using System;
using System.Collections.Generic;
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
        private List<Comment> comments;
        private List<Like> likes;

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
        public string VideoLink
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
            this.postOwner = postOwner;
            this.postContent = postContent;
            this.videoLink = videoLink;
            this.comments = new List<Comment>();
            this.likes = new List<Like>();
        }

        public Post(User postOwner, string postContent)
        {
            this.postOwner = postOwner;
            this.postContent = postContent;
            this.videoLink = "";
            this.comments = new List<Comment>();
            this.likes = new List<Like>();
        }
    }
}
