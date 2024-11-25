using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Simulation_2.Stages.Stage1
{
    internal class Post
    {
        private User postOwner;
        private string postContent;
        private string videoLink;
        private IList<Comment> comments;
        private IList<Like> likes;

        public User PostOwner
        {
            get { return this.postOwner; }
            set { this.postOwner = value; }
        }
        public string PostContent
        {
            get { return this.postContent; }
            set { this.postContent = value; }
        }
        public string? VideoLink
        {
            get { return this.videoLink; }
            set { this.videoLink = value; }
        }
        public IList<Comment> Comments
        {
            get { return this.comments; }
            set { this.comments = value; }
        }
        public IList<Like> Likes
        {
            get { return this.likes; }
            set { this.likes = value; }
        }

        public Post(User postOwner, string postContent, string videoLink)
        {
            this.__Post(postOwner, postContent);
            this.videoLink = videoLink;
        }
        public Post(User postOwner, string postContent)
        {
            this.__Post(postOwner, postContent);
            this.videoLink = null;
        }
        private void __Post(User postOwner, string postContent)
        {
            // This function was created in order to handle with duplication of code in the "Post" functions.
            this.postOwner = postOwner;
            this.postContent = postContent;
            this.comments = new List<Comment>();
            this.likes = new List<Like>();
        }
    }
}
