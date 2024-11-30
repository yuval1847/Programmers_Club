using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Classes
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
        private IList<FriendRequest> friendRequests;
        // private IList<Chat> chats;


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
            this.friendRequests = new List<FriendRequest>();
        }

        public void AddNewFriend(User newFriend)
        {
            this.friends.Add(newFriend);
        }

        public IList<FriendRequest> GetFriendRequests()
        {
            return this.friendRequests;
        }

        public void OfferFriendRequest(FriendRequest friendRequest)
        {
            this.friendRequests.Add(friendRequest);
        }

        public void FriendRequestManagement(FriendRequest friendRequest, RequestStatus requestStatus)
        {
            friendRequest.UpdateRequestStatus(requestStatus);           
        }

        public bool IsFriend(User user)
        {
            return this.friends.Contains(user);
        }
        
        
    }
}
