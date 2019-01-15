import sys
# import logging as Logger
import ClientController

# Helper variables, functions & logging
main_commands = ['client', 'exit']


def client_loop():
    client_commands = [ 'list', 'create', 'start', 'stop', 'publish' ]
    print('\nClient Interface --Help')
    while True:
        command = input('>>')

        if command == '':
            pass
        # Help for client interface
        elif command.lower() == 'help':
            print(', '.join(client_commands))
        # List Idle & Running Clients
        elif command.lower() == 'list':
            [idle, running] = ClientController.get_clients()
            print('Idle Clients:')
            print(', '.join(idle))
            print('Running Clients:')
            print(', '.join(running))
        # Create a new client
        elif command.lower() == 'create':
            name = input('Name: ')
            broker = input('Broker address: ')
            topics = input('(Space Delimited) Topics: ').split(" ")
            if broker == '' or broker == None:
                if ClientController.create_client(name, topics) == 0:
                    print(name + ' created...')
                else:
                    print('Unable to create client...')
            else:
                if ClientController.create_client(name, topics, broker) == 0:
                    print(name + ' created...')
                else:
                    print('Unable to create client...')
        # Start an idle client
        elif command.lower() == 'start':
            name = input('Client ID:')
            if ClientController.start_client(name):
                print(name + ' started...')
            else:
                print('Error occurred!')
        # Stop running client
        elif command.lower() == 'stop':
            name = input('Client ID:')
            if ClientController.stop_client(name):
                print(name + ' stopped...')
            else:
                print('Error occurred!')
        # Publish using given client
        elif command.lower() == 'publish':
            name = input('Client ID:')
            topic = input('Topic:')
            msg = input('Message:')
            if ClientController.publish_client(name, topic, msg):
                print('Publish Successful')
            else:
                print('Publish Failure')

        # Exit client interface
        elif command.lower() == 'exit':
            break
        else:
            print("Command '" + command + "' not recognized")    


# Program start
print('Server Interface Started --Help')
while True:
    command = input('>>')

    # Parse input
    if command == '':
        pass
    elif command.lower() == "help":
        print(', '.join(main_commands))
    elif command.lower() == "client":
        client_loop()
    elif command.lower() == "exit":
        break
    else:
        print("Command '" + command + "' not recognized")

# Hit end of program, exit
sys.exit(0)
