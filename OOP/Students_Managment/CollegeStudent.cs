using System;
using StudentNameSpace;

namespace CollegeStudentNameSpace
{
    public class CollegeStudent : Student
    {
        // A class which represents a college student.
        protected string subject;
        protected int avg;

        public CollegeStudent(string studentName, int studentID, int age, string subject, int avg)
            : base(studentName, studentID, age)
        {
            this.subject = subject;
            this.avg = avg;
        }

        public string GetSubject()
        {
            return this.subject;
        }

        public int GetAvg()
        {
            return this.avg;
        }

        public void SetSubject(string subject)
        {
            this.subject = subject;
        }

        public void SetAvg(int avg)
        {
            this.avg = avg;
        }

        public override void DisplayInformation()
        {
            Console.WriteLine("******* College Student Info ***********");
            Console.WriteLine($"Name: {this.studentName}\nID: {this.studentID}\nAge: {this.age}\nSubject: {this.subject}\nGrades Avg: {this.avg}");
        }
    }
}
