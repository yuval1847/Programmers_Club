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
        
        public void SendFriendRequest(User sender, User receiver)
        {
            FriendRequest friendRequest = new FriendRequest(sender, receiver);
            friendRequest.Approve();
        }

        public IList<IList<Post>> GetPostsOfUser(User user)
        {
            IList<Post> postsWithVideoLink = new List<Post>();
            IList<Post> postsWithoutVideoLink = new List<Post>();
            foreach (var post in this.Posts)
            {
                if (post.PostOwner == user)
                {
                    if (post.VideoLink != null)
                    {
                        postsWithVideoLink.Add(post);
                    }
                    else
                    {
                        postsWithoutVideoLink.Add(post);
                    }
                }
            }
            IList<IList<Post>> allPosts = new List<IList<Post>>();
            allPosts.Add(postsWithVideoLink);
            allPosts.Add(postsWithoutVideoLink);
            return allPosts;
        }

    }
}
