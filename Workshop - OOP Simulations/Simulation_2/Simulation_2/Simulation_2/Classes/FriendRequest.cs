using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Classes
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
        private string meetingMessage;
        public FriendRequest(User sender, User receiver, string meetingMessage)
        {
            this.sender = sender;
            this.receiver = receiver;
            this.meetingMessage = meetingMessage;
            this.requestStatus = RequestStatus.Waiting;
        }

        public void Approve()
        {
            this.UpdateRequestStatus(RequestStatus.Approved);
            this.sender.AddNewFriend(this.receiver);
            this.receiver.AddNewFriend(this.sender);
        }

        public void Decline()
        {
            this.UpdateRequestStatus(RequestStatus.Declined);
        }

        public void UpdateRequestStatus(RequestStatus requestStatus)
        {
            this.requestStatus = requestStatus;
        }
    }
}
