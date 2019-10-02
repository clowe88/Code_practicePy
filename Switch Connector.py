import warnings
with warnings.catch_warnings(record=True) as w:
    import paramiko

import multiprocessing
from datetime import datetime

import sys
from getpass import getpass

import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

# DEVICE_CREDS contains the devices to connect to
from DEVICE_CREDS import all_devices

def print_output(results):

    print "\nDevices:"
    for a_res in results:
        for identifier,v in a_res.iteritems():
            (success, out_string) = v['error']
            if success:
                print 'Device failed = {0}'.format(identifier)
                print '\n\tError: '.out_string
            else:
                print '\n'
                print '#' * 80
                print 'Device success = {0}\n'.format(identifier)
                for c,r in v['results'].iteritems():
                    print '\tCommand: ' +   c
                    print '\n\tResult: '+ r
                print '#' * 80

    print "\nEnd time: " + str(datetime.now())
    print

def worker_configuration(a_device, mp_queue):

    try:
        a_device['conf']['port']
    except KeyError:
        a_device['conf']['port'] = 22

    r_time = datetime.now()
    save_command = 'show running-config'
    identifier = '{ip}'.format(**a_device['conf'])
    return_data = {}

    SSHClass = netmiko.ssh_dispatcher(a_device['conf']['device_type'])

    try:
        #print 'Device: ' + a_device['conf']['device_type'];
        a_dev = a_device['conf']
        net_connect = SSHClass(**a_dev)
        return_data[identifier] = {}
        return_data[identifier]['results'] = {}
        #print '\nPrompt: ' + net_connect.find_prompt()
        for command in a_device['commands']:
            #print '\nCommand: ' + command
            result = net_connect.send_command(command)
            #print '\nResult: ' + result
            return_data[identifier]['results'][command] = result
            if command == save_command:
                f= open('/home/Firewalls-Backup/'+identifier+'.txt',"w+")
                f.write(result)
                f.close()
        return_data[identifier]['error'] = (False, 'Success')
        net_connect.disconnect()
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return_data[identifier]['error'] = (True, e)

        # Add data to the queue (for parent process)
        mp_queue.put(return_data)
        return None
    mp_queue.put(return_data)
def main():

    #user = raw_input("Enter Cisco user: ")
    #passwd =  getpass("Insert password: ")
    mp_queue = multiprocessing.Queue()
    processes = []

    print "\nStart time: " + str(datetime.now())

    for a_device in all_devices:
        #a_device['conf']['username']  = user
        #a_device['conf']['password'] =  passwd
        p = multiprocessing.Process(target=worker_configuration, args=(a_device, mp_queue))
        processes.append(p)
        # start the work process
        p.start()

    # wait until the child processes have completed
    for p in processes:
        p.join()

    # retrieve all the data from the queue
    results = []

    for p in processes:
        results.append(mp_queue.get())


    print_output(results)


if __name__ == '__main__':

    main()