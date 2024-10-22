from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<user_name>:<password><hostname>/", tlsAllowInvalidCertificates=True)


print(client)
db = client["my-python-projects-rahul"]
task_collection = db["tasks_manager"]


def list_all_tasks():
    for task in task_collection.find():
        print(f'''
        task_id: {task['_id']}, 
        task_name: {task['task_name']} ,
        task_priority:{task['task_priority']},
        task_type:{task['task_type']},
        task_total_time:{task['task_total_time']},
        task_spent_time:{task['task_spent_time']},
        task_current_status:{task['task_current_status']},
        task_eta:{task['task_eta']},
        task_comments:{task['task_comments']}'''
        )

def add_task(task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,task_comments):
    task_collection.insert_one({"task_name": task_name,
                                "task_priority": task_priority,
                                "task_type": task_type,
                                "task_total_time": task_total_time,
                                "task_spent_time": task_spent_time,
                                "task_current_status": task_current_status,
                                "task_eta": task_eta,
                                "task_comments": task_comments

})

def update_task(task_id,task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,task_comments):
    task_collection.update_one({'_id': ObjectId(task_id)},
                                {
                                    "$set":
                                {
                                    "task_name": task_name,
                                    "task_priority": task_priority,
                                    "task_type": task_type,
                                    "task_total_time": task_total_time,
                                    "task_spent_time": task_spent_time,
                                    "task_current_status": task_current_status,
                                    "task_eta": task_eta,
                                    "task_comments": task_comments
 }})

def delete_task(task_id):
    task_collection.delete_one({'_id': ObjectId(task_id)})





def main():
    while True:
        print("\nMy personal task manager :")
        print("\n1. List all  tasks")
        print("2. Add task")
        print("3. update task")
        print("4. delete task")
        print("5. Exit application: ")
        choice=input("\nPlease enter your choice: \n")

        if choice=='1':
           list_all_tasks()
        elif choice=='2':
            task_name=input("Enter task name: ")
            task_priority=input("Enter task priority (P1-P4): ")
            task_type=input("Enter task category (Personal/Professional) : ")
            task_total_time=input("Enter hrs required to complete task: ")
            task_spent_time=input("Enter hrs spent on task: ")
            task_current_status=input("Enter current status of task: ")
            task_eta=input("Enter ETA of task in (YYYY-MM-DD) format: ")
            task_comments=input("Enter comments, if any : ")
            add_task(task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments)
        elif choice=='3':

            list_all_tasks()
            task_id=input("Enter task_id to update task: ")
            task_name = input("Enter new task name: ")
            task_priority = input("Enter new task priority (P1-P4): ")
            task_type = input("Enter  new task category (Personal/Professional) : ")
            task_total_time = input("Enter hrs required to complete task: ")
            task_spent_time = input("Enter hrs spent on task: ")
            task_current_status = input("Enter current status of task: ")
            task_eta = input("Enter ETA of task in (YYYY-MM-DD) format: ")
            task_comments = input("Enter comments, if any : ")
            update_task(task_id,task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments)
        elif choice=='4':
            list_all_tasks()
            task_id = input("Enter task_id to be deleted : ")
            delete_task(task_id)
        elif choice =='5':
            break
        else:
            print("Please enter valid choice: ")


if __name__=="__main__":
    main()

