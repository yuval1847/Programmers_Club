using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Stages.Stage1
{
    internal class Facebook : SocialPlatform
    {
        public Facebook():base()
        {
            
        }
        public void SendFriendInvitation(User sender, User invitedFriend)
        {
            sender.Friends.Add(invitedFriend);
            invitedFriend.Friends.Add(sender);
        }
        public void GetFeed(User user)
        {
            IList<Post> feed = new List<Post>();
            foreach(var friend in user.Friends)
            {
                feed.Add(GetPostsOfUser(friend));
            }
        }
    }
}
