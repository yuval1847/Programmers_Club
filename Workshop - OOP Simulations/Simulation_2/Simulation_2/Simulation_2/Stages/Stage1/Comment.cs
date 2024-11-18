using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Stages.Stage1
{
    internal class Comment
    {
        private User commentWriter;
        private string commentContent;
        private static int commentsAmount = 0;
        private int commentId;
        public User CommentWriter
        {
            get { return this.commentWriter; }
        }
        public string CommentContent
        {
            get { return this.commentContent; }
            set { this.commentContent = value; }
        }
        public int CommentId
        {
            get { return this.commentId; }
        }

        public Comment(User commentWriter, string commentContent)
        {
            this.commentWriter = commentWriter;
            this.commentContent = commentContent;
            // The function just increase the parameter by 1 and return it.
            commentId = Interlocked.Increment(ref commentsAmount);
        }
    }
}
