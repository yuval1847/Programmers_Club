using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Stages.Stage1
{
    internal enum UserRelationStatus
    {
        Single,
        Married,
        Divorced
    }
    internal class User
    {
        private string firstName;
        private string lastName;
        private int age;
        private UserRelationStatus relationStatus;
        private IList<User> friends;

        public string FirstName
        {
            get { return this.firstName; }
            set { this.firstName = value; }
        }
        public string LastName
        {
            get { return this.lastName; }
            set { this.lastName = value; }
        }
        public int Age
        {
            get { return this.age; }
            set { this.age = value; }
        }
        public UserRelationStatus RelationStatus
        {
            get { return this.relationStatus; }
            set { this.relationStatus = value; }
        }
        public IList<User> Friends
        {
            get { return this.friends; }
            set { this.friends = value; }
        }

        public User(string firstName, string lastName, int age, UserRelationStatus relationStatus)
        {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.relationStatus = relationStatus;
            this.friends = new List<User>();
        }
    }
}
