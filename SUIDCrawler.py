#!/usr/bin/python3

import argparse
import os
import sys
import subprocess

def printf(message, *argv):
    ''' 
    Printfunction to show formated all output.
    @param message will be the message to print.
    @param args will be a list of messages/entries to print with the message param.
    '''
    for entry in argv: print("[+] {0} - {1}".format(message, entry))

def printE(error, exit_t, *argv):
    '''
    Function to print an error in case one occurs and exit incase exit is set to true.
    @param error will be the error message (Not the Exception message).
    @param exit_t incase exit is true after an exception the program will return/exit directly.
    @param argv will be a args-vektor for multiple error messages. 
    '''
    for entry in argv: print("[-] An error occured - Message: {} - Exception: {}".format(error, entry))
    if exit_t: sys.exit()

def writeToFile(message, path):
    ''' 
    Function to write to. This function will write all findings in the given file.
    @param path will be the path to the file (complete direcotry).
    @param message will be the line to write into the file.
    '''
    try:
        with open(path, 'a') as outputfile:
            outputfile.write(message + "\n")
    except Exception as error:
        printE("An error occured while trying to write into the output file.", True, error)

def verboseFileInformation(path):   
    '''
    Function to verbose more information about the file, found by the crawler.
    @param will be the path to the file.
    '''
    try:
        os.system("ls -lisan {}".format(path))
    except Exception as error:
        printE("An error occured while trying to find more information about a file", error)

def runCommand(user, path, outputPath, verbose):
    '''
    Function to run the command to find all suidprograms.
    @param user will be the user to run search for
    @param path will be the path to run from 
    @param outputpath will be the path/file to write to.
    '''
    try:
        output = ""
        for entry in subprocess.getoutput("find {} -user {} -perm -4000 2>/dev/null".format(path, user)): 
            if not entry == '\n':
                output = output + str(entry)
            else:
                if os.path.isfile(output): 
                    printf("Found ", output)
                    writeToFile(output, outputPath)
                    if verbose: verboseFileInformation(output)
                output = ""
    except Exception as error:
        printE("An error occured while trying to find all SUID files", error)

def handleArguments(args):
    '''
    Function to handle given arguments.
    @param args will be the result of the argparser-modul.
    @return will return dict. with arguments. 
    '''
    return vars(args)

def main():
    ''' Main-Function '''
    parser = argparse.ArgumentParser(description='Argumentparser for all SUID-Program args.')
    parser.add_argument('-path',
                        help="Path form where to start. Default will be the root-directory.",
                        default="/",
                        )
    parser.add_argument('-output', 
                        help="Will be a file to put in all suid programms with the path. Please enter a complete path to your file. E.g /home/user/output.txt"
                        )
    parser.add_argument('-user', 
                        help="Will be the user to search for. Default is root.",
                        default="root"
                        )
    parser.add_argument('-verbose', 
                        help="Will be the user to search for. Default is root.",
                        action='store_true'
                        )
    args = handleArguments(parser.parse_args())
    runCommand(args['user'], args['path'], args['output'], args['verbose'])

if __name__ == "__main__":
    ''' Mainfunction call. '''
    main()