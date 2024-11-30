using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Classes
{
    internal class Chat
    {
        private IList<User> members;
        private Queue<Message> messages;

        private bool IsAllMembersAreFriend()
        {
            for (int i = 0; i < this.members.Count; i++)
            {
                for(int j = 0; j < this.members.Count; j++)
                {
                    if (this.members[i] != this.members[j] && !this.members[i].IsFriend(this.members[j])) { return false; }
                }
            }
            return true;
        }
        public Chat(IList<User> members)
        {
            this.members = members;
            if (!this.IsAllMembersAreFriend())
            {
                throw new ArgumentException("All the chat members have to be friends!");
            }
            this.messages = new Queue<Message>();
        }

        public void SendMessage(Message message)
        {
            if (this.IsMember(message.Sender))
            {
                this.AddMessage(message);
            }
        }
        private bool IsMember(User user)
        {
            return this.members.Contains(user);
        }
        private void AddMessage(Message message)
        {
            this.messages.Enqueue(message);
        }
       
    }
}
