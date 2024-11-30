using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Classes
{
    internal class Message
    {
        private User sender;
        private string content;
        private Time sendingTime;

        public User Sender
        {
            get { return this.sender; }
        }
        public string Content
        {
            get { return this.content; }
        }
        public Time SendingTime
        {
            get { return this.sendingTime; }
        }
        public Message(User sender, string content, Time sendingTime)
        {
            this.sender = sender;
            this.content = content;
            this.sendingTime = sendingTime;
        }
    }
}
