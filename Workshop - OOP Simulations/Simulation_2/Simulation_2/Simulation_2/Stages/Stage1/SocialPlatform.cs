using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Stages.Stage1
{
    internal abstract class SocialPlatform
    {
        private IList<User> users;
        private IList<Post> posts;

        public SocialPlatform()
        {
            this.users = new List<User>();
            this.posts = new List<Post>();
        }

        public void PublishNewPost(User publisher, string content) 
        {
            this.posts.Add(new Post(publisher, content));
        }
        public void PublishNewPost(User publisher, string content, string videoLink)
        {
            this.posts.Add(new Post(publisher, content, videoLink));
        }
    }
}
