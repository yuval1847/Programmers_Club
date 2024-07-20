using System;
using IPersonNameSpace;

namespace StudentNameSpace
{
    public class Student : IPerson
    {
        // A class which represents a student.
        protected string studentName;
        protected int studentID;
        protected int age;

        public Student(string studentName, int studentID, int age)
        {
            this.studentName = studentName;
            this.studentID = studentID;
            this.age = age;
        }

        // Get & Set functions.
        public string GetStudentName()
        {
            return this.studentName;
        }

        public int GetStudentID()
        {
            return this.studentID;
        }

        public int GetAge()
        {
            return this.age;
        }

        public void SetStudentName(string studentName)
        {
            this.studentName = studentName;
        }

        public void SetStudentID(int id)
        {
            this.studentID = id;
        }

        public void SetAge(int age)
        {
            this.age = age;
        }

        public (string studentName, int id, int age) GetStudentInfo()
        {
            // The function gets nothing.
            // The function returns a tuple which contains the student's info
            return (studentName, studentID, age);
        }

        public virtual void DisplayInformation()
        {
            Console.WriteLine("******* Student Info ***********");
            Console.WriteLine($"Name: {this.studentName}\nID: {this.studentID}\nAge: {this.age}");
        }
    }
}
