# Signals

## What is it?
The signal python library is used to trigger events like SIGKILL events.

Those event can be sent by the system or by you in python.

Some possibilities:
* Do a specific action if the program is running for more than x seconds.
* Do a specific action if the system try to kill your process.
* Kill gracefully your process.
* Kill your process now.
* Detect when there is an error
* ...

## How to use it?
* First you can look at the [official documentation](https://docs.python.org/3/library/signal.html)
* Then I strongly recommand you to read this [well made article](https://www.journaldev.com/16039/python-signal-processing).
* See [how to gracefully kill a process programmaticly](https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python).

## Usage example
Let's say that you want to print a warning when your code run for more than 20sec (or kill the process, run another function,...).

You could do something like that:

```python
import signal  
import time  

def alarm_handler(signum, stack):
    """Function that will run when you alarm trigger."""  
    print('Alarm at:', time.ctime())  
  
# Assign alarm_handler to SIGALARM  
signal.signal(signal.SIGALRM, alarm_handler)
# set alarm after 20 seconds
signal.alarm(20)
# Print the current time
print('Time:', time.ctime())  
# Make your code run for more than 20sec
time.sleep(30) 
```
