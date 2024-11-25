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

        public IList<User> Users
        {
            get { return this.users; }
            set { this.users = value; }
        }
        public IList<Post> Posts
        {
            get { return this.posts; }
            set { this.posts = value; }
        }

        public SocialPlatform()
        {
            this.users = new List<User>();
            this.posts = new List<Post>();
        }

        public void PublishNewPost(User publisher, string content) 
        {
            Post newPost = new Post(publisher, content);
            this.__NewPost(newPost);
        }
        public void PublishNewPost(User publisher, string content, string videoLink)
        {
            Post newPost = new Post(publisher, content, videoLink);
            this.__NewPost(newPost);
        }
        private void __NewPost(Post p)
        {
            // This function was created in order to handle with duplication of code in the "new post" functions.
            this.posts.Add(p);
        }
        
        public IList<Post> GetPostsOfUser(User user)
        {
            IList<Post> postsOfUser = new List<Post>();
            foreach (var post in this.posts)
            {
                if(post.PostOwner == user)
                {
                    postsOfUser.Add(post);
                }
            }
            return postsOfUser;
        }
    }
}
