using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Classes
{
    internal class Facebook : SocialPlatform
    {
        public Facebook():base()
        {
            
        }
        public IList<Post> GetFeed(User user)
        {
            IList<Post> feedWithVideos = new List<Post>();
            IList<Post> feedWithoutVideos = new List<Post>();
            IList<IList<Post>> currentFriendPosts = new List<IList<Post>>(); 
            foreach(var friend in user.Friends)
            {
                currentFriendPosts = this.GetPostsOfUser(friend);
                feedWithVideos = feedWithVideos.Concat(currentFriendPosts[0]).ToList();
                feedWithoutVideos = feedWithoutVideos.Concat(currentFriendPosts[1]).ToList();
            }
            return feedWithVideos.Concat(feedWithoutVideos).ToList();
        }
    }
}