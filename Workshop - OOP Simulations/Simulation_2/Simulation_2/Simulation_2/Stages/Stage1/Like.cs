using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Stages.Stage1
{
    internal class Like
    {
        private User liker;
        private static int likesAmount = 0;
        private int likeId;

        public User Liker
        {
            get { return this.liker; }
        }
        public Like(User liker)
        {
            this.liker = liker;
            likeId = Interlocked.Increment(ref likesAmount);
        }
    }
}
