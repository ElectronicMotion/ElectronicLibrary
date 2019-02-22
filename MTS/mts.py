import sys
import sqlite3
import time

con = sqlite3.connect('mts.db')
c = con.cursor()


def outputdata(data, report):

    print("#-- " + report + " --------------------\n|")
    for x in range(len(data)):
        date = str(data[x][4])
        state = str(data[x][3])
        id = str(data[x][0])
        title = str(data[x][1])
        text = str(data[x][2])
        if state == "Open":
            state = "Open  "

        if int(id) < 100:
            if int(id) < 10:
                id = " " + id + " "
            else:
                id = " " + id

        output = '| * ' + date + '  ' + id + '  ' + state + '  ' + title + '\n|   ' + text
        print(output)
    print ("|\n#----------------------------------")


def outputcomments(data, report):
    print("#-- " + report + " ----------------------\n|")
    if report == 'All comments':
        if data:
            for x in range(len(data)):
                date = str(data[x][3])
                text = str(data[x][2])
                task = str(data[x][1])
                output = '| * ' + date + '  ' + task + '  ' + text
                print(output)
        else:
            print("| No Comments.")

    else:
        if data:
            for x in range(len(data)):
                date = str(data[x][3])
                text = str(data[x][2])
                output = '| * ' + date + '  ' + text
                print(output)
        else:
            print("| No Comments.")
    print("|\n#----------------------------------")


if len(sys.argv) == 1:
    c.execute("SELECT * FROM tasks WHERE Status = 'Open'")
    data = c.fetchall()
    outputdata(data, "Open Tasks")
else:
    if sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Error: Please add Title and Description.")
        if len(sys.argv) < 4:
            print("Error: Please add Description.")
        if len(sys.argv) == 4:
            cmd = "INSERT INTO tasks (Title, Description, Status, Date) VALUES ('" + str(sys.argv[2]) + "', '" + str(sys.argv[3]) + "', 'Open', '" + time.strftime("%d-%m-%y") + "');"
            c.execute(cmd)

    if sys.argv[1] == "del":
        if len(sys.argv) < 3:
            print("Error: please add Ticket-ID")
        else:
            c.execute("DELETE from tasks WHERE ID == " + sys.argv[2])

    if sys.argv[1] == "close":
        if len(sys.argv) < 3:
            print("Error: please add Ticket-ID")
        else:
            c.execute("UPDATE tasks SET status = 'Closed' WHERE status = 'Open' AND ID ='" + sys.argv[2] + "';")

    if sys.argv[1] == "comment":
        if len(sys.argv) < 3:
            print("Error: Please provide Task-ID and comment.")
        else:
            if len(sys.argv) < 4:
                print("Error: Please provide comment.")
            else:
                cmd = "INSERT INTO comments (TaskID, Comment, DATE) VALUES ('" + sys.argv[2] + "', '" + sys.argv[3] + "', '" + time.strftime("%d-%m-%y") + "');"
                c.execute(cmd)
                print("Added comment.")

    if sys.argv[1] == "show":
        if len(sys.argv) < 3:
            print("Error: Please specifiy what to show.")
        else:
            if sys.argv[2] == "all":
                c.execute("SELECT * FROM tasks")
                data = c.fetchall()
                outputdata(data, "All Tasks")

            if sys.argv[2] == "closed":
                c.execute("SELECT * FROM tasks WHERE status = 'Closed'")
                data = c.fetchall()
                outputdata(data, "Closed Tasks")

            if sys.argv[2] == "comments":
                if len(sys.argv) < 4:
                    print("Error: Please provide Task-ID")
                else:
                    if sys.argv[3] == 'x' or sys.argv[3] == 'X':
                        c.execute("SELECT * from comments")
                        data = c.fetchall()
                        outputcomments(data, "All comments")
                    else:
                        c.execute("SELECT * from comments WHERE TaskID == " + sys.argv[3])
                        data = c.fetchall()
                        outputcomments(data, "comments")

    if sys.argv[1] == "init":
        c.execute("CREATE TABLE tasks("
                  "ID integer PRIMARY KEY autoincrement, "
                  "Title TEXT NOT NULL, "
                  "Description TEXT NOT NULL, "
                  "Status TEXT NOT NULL, "
                  "DATE TEXT NOT NULL)")
        c.execute("CREATE TABLE comments("
                  "ID integer PRIMARY KEY autoincrement, "
                  "TaskID INT NOT NULL, "
                  "Comment TEXT NOT NULL, "
                  "DATE TEXT NOT NULL)")

    if sys.argv[1] == "help":
        print("# -- List of commands---------------")
        print("| init       Initialises a db file.")
        print("|            Only needed once!")
        print("| add        Adds a new taks.")
        print("|            add \"Title\" \"Description\"")
        print("| show       Can show different stuff.")
        print("|   all      Displays all Tasks in db")
        print("|   closed   Displays all closed tasks")
        print("|   comments Displays all comments related to a task")
        print("|            show comments [TaskID]")
        print("|            If x is provided as TaskID, all comments will be shown.")
        print("| comment    Adds a comment to a task")
        print("|            comment [TaskID] \"Comment\"")
        print("| del        Deletes a Task")
        print("|            del [TaskID]")
        print("| close      Sets a Tasks status to closed")
        print("|            close [TaskID]")
        print("# ----------------------------------")

con.commit()
con.close()
