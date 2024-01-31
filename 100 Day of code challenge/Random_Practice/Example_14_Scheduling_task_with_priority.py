from collections import deque

class Task(object):
    def __init__(self, tasDesc, hasPriority=False):
        self.taskDesc = tasDesc
        self.hasPriority = hasPriority
    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

tas_queue = deque()
def add_task(task):
    if task.hasPriority:
        tas_queue.appendleft(task)
    else:
        tas_queue.append(task)

def do_task():
    return tas_queue.popleft()

def print_tasks():
    for t in tas_queue:
        print(t.taskDesc)

def main():
    add_task(Task("Make List"))
    add_task(Task("Make Breakfast"))
    add_task(Task("Respond to email", True))
    print_tasks()
    print(do_task())
    return

if __name__ == '__main__':
    main()