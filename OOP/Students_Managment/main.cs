using System;
using StudentNameSpace;
using CollegeStudentNameSpace;

class Program
{
    private static Student[] studentsArr = new Student[0];
    private static CollegeStudent[] collegeStudentsArr = new CollegeStudent[0];

    public static void AddToArr(Student s = null, CollegeStudent cs = null)
    {
        // The function gets an object of a student or a college student.
        // The function adds the student to the appropriate array.
        if (s != null)
        {
            Array.Resize(ref studentsArr, studentsArr.Length + 1);
            studentsArr[studentsArr.Length - 1] = s;
        }
        else if (cs != null)
        {
            Array.Resize(ref collegeStudentsArr, collegeStudentsArr.Length + 1);
            collegeStudentsArr[collegeStudentsArr.Length - 1] = cs;
        }
    }

    public static int IndexById(int id, int type)
    {
        // The function gets an integer which represents an id of a student and an integer value which represents a 
        // regular student(1) or a college one(2).
        // The function returns the index of the student in the appropriate array but if it doesn't exist the function
        // returns -1.
        if (type == 1)
        {
            for (int i = 0; i < studentsArr.Length; i++)
            {
                if (studentsArr[i].GetStudentID() == id)
                {
                    return i;
                }
            }
        }
        else if (type == 2)
        {
            for (int i = 0; i < collegeStudentsArr.Length; i++)
            {
                if (collegeStudentsArr[i].GetStudentID() == id)
                {
                    return i;
                }
            }
        }
        return -1;
    }

    public static int MakeAChoice()
    {
        // The function gets nothing.
        // The function returns user's action choice
        Console.WriteLine("\n*********************\nHere is your menu:\n0.Exit\n1.Register\n2.Change details\n3.Show details\n*********************\n");
        Console.WriteLine("Choose your action:");
        int choice;
        while (!int.TryParse(Console.ReadLine(), out choice) || !(0 <= choice && choice <= 3))
        {
            Console.WriteLine("Choose your action (between 0-3):");
        }
        return choice;
    }

    public static void Register()
    {
        // The function gets nothing.
        // The function returns a student object with the user's input.
        Console.WriteLine("Are you a regular or college student (1-regular, 2-college):");
        int isCollege;
        while (!int.TryParse(Console.ReadLine(), out isCollege) || !(1 <= isCollege && isCollege <= 2))
        {
            Console.WriteLine("Please enter 1 or 2!");
        }
        Console.WriteLine("Enter your name:");
        string name = Console.ReadLine();
        Console.WriteLine("Enter your id:");
        int id = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter your age:");
        int age = int.Parse(Console.ReadLine());
        if (isCollege == 2)
        {
            Console.WriteLine("Enter your subject:");
            string subject = Console.ReadLine();
            Console.WriteLine("Enter the avg of your grades:");
            int avg = int.Parse(Console.ReadLine());
            AddToArr(cs: new CollegeStudent(name, id, age, subject, avg));
        }
        else
        {
            AddToArr(new Student(name, id, age));
        }
    }

    public static void ChangeDetails()
    {
        // The function gets nothing.
        // The function changes a student's details according to the user's requirements.
        Console.WriteLine("Are you a regular or college student (1-regular, 2-college):");
        int isCollege;
        while (!int.TryParse(Console.ReadLine(), out isCollege) || !(1 <= isCollege && isCollege <= 2))
        {
            Console.WriteLine("Please enter 1 or 2!");
        }
        Console.WriteLine("Enter your id:");
        int id = int.Parse(Console.ReadLine());
        int studentIndex = IndexById(id, isCollege);

        if (studentIndex != -1)
        {
            if (isCollege == 1)
            {
                Console.WriteLine("Possible details:\n1.name\n2.id\n3.age\nChoose the detail that you want to change:");
                int choice;
                while (!int.TryParse(Console.ReadLine(), out choice) || !(1 <= choice && choice <= 3))
                {
                    Console.WriteLine("Choose your action (between 1-3):");
                }
                switch (choice)
                {
                    case 1:
                        Console.WriteLine("Enter the new name:");
                        studentsArr[studentIndex].SetStudentName(Console.ReadLine());
                        break;
                    case 2:
                        Console.WriteLine("Enter the new id:");
                        studentsArr[studentIndex].SetStudentID(int.Parse(Console.ReadLine()));
                        break;
                    case 3:
                        Console.WriteLine("Enter the new age:");
                        studentsArr[studentIndex].SetAge(int.Parse(Console.ReadLine()));
                        break;
                }
            }
            else
            {
                Console.WriteLine("Possible details:\n1.name\n2.id\n3.age\n4.subject\n5.avg\nChoose the detail that you want to change:");
                int choice;
                while (!int.TryParse(Console.ReadLine(), out choice) || !(1 <= choice && choice <= 5))
                {
                    Console.WriteLine("Choose your action (between 1-5):");
                }
                switch (choice)
                {
                    case 1:
                        Console.WriteLine("Enter the new name:");
                        collegeStudentsArr[studentIndex].SetStudentName(Console.ReadLine());
                        break;
                    case 2:
                        Console.WriteLine("Enter the new id:");
                        collegeStudentsArr[studentIndex].SetStudentID(int.Parse(Console.ReadLine()));
                        break;
                    case 3:
                        Console.WriteLine("Enter the new age:");
                        collegeStudentsArr[studentIndex].SetAge(int.Parse(Console.ReadLine()));
                        break;
                    case 4:
                        Console.WriteLine("Enter the new subject:");
                        collegeStudentsArr[studentIndex].SetSubject(Console.ReadLine());
                        break;
                    case 5:
                        Console.WriteLine("Enter the new grades avg:");
                        collegeStudentsArr[studentIndex].SetAvg(int.Parse(Console.ReadLine()));
                        break;
                }
            }
            Console.WriteLine("The details have been updated successfully!");
        }
        else
        {
            Console.WriteLine("The entered id doesn't exist!");
        }
    }

    public static void ShowDetails()
    {
        // The function gets nothing.
        // The function shows the appropriate student's info to the user.
        Console.WriteLine("Are you a regular or college student (1-regular, 2-college):");
        int isCollege;
        while (!int.TryParse(Console.ReadLine(), out isCollege) || !(1 <= isCollege && isCollege <= 2))
        {
            Console.WriteLine("Please enter 1 or 2!");
        }
        Console.WriteLine("Enter your id:");
        int id = int.Parse(Console.ReadLine());
        int studentIndex = IndexById(id, isCollege);
        if (studentIndex == -1)
        {
            Console.WriteLine("The entered id doesn't exist!");
        }
        else
        {
            if (isCollege == 1)
            {
                studentsArr[studentIndex].DisplayInformation();
            }
            else
            {
                collegeStudentsArr[studentIndex].DisplayInformation();
            }
        }
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("Welcome to the Students Union!");
        while (true)
        {
            int choice = MakeAChoice();
            switch (choice)
            {
                case 0:
                    return;
                case 1:
                    Register();
                    break;
                case 2:
                    ChangeDetails();
                    break;
                case 3:
                    ShowDetails();
                    break;
            }
        }
    }
}
