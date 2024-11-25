using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Stages.Stage1
{
    enum RequestStatus
    {
        Waiting,
        Approved,
        Declined
    }

    internal class FriendRequest
    {
        private User sender;
        private User receiver;
        private RequestStatus requestStatus;
        public FriendRequest(User sender, User receiver)
        {
            this.sender = sender;
            this.receiver = receiver;
            this.requestStatus = RequestStatus.Waiting;
        }

        public void Approve()
        {
            this.requestStatus = RequestStatus.Approved;
            this.sender.AddNewFriend(this.receiver);
            this.receiver.AddNewFriend(this.sender);
        }
    }
}
