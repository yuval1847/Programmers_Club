using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Simulation_2
{
    public class User
    {
        private string firstName;
        private string lastName;
        private int age;
        private string maritalStatus;

        public string FirstName{
            get{ return this.firstName; }
            set{ this.firstName = value; }
        }
        public string LastName{
            get{ return this.lastName; }
            set{ this.lastName = value; }
        }
        public int Age{
            get{ return this.age; }
            set{ this.age = value; }
        }
        public string MaritalStatus{
            get{ return this.maritalStatus;}
            set
            { 
                if (value == "single" || value == "divorcee" || value == "married")
                {
                    this.maritalStatus = value; 
                }
                else
                {
                    throw new ArgumentException("The marital status need to be only single\divorcee\married!");
                }
            }
        }

        public User(string firstName, string lastName, int age, string maritalStatus){
            try
            {
                this.FirstName = firstName;
                this.LastName = lastName;
                this.Age = age;
                this.MaritalStatus = maritalStatus;
            }
            catch(Exception ex)
            {
                Console.WriteLine($"Exception Caught: {exex.Message}");
            }
        }
        
    }
}