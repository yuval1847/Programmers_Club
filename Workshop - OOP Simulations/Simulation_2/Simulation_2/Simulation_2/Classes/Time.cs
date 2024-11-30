using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simulation_2.Classes
{
    internal class Clock
    {
        private int second;
        private int min;
        private int hour;

        public Clock(int second, int min, int hour)
        {
            this.second = second;
            this.min = min;
            this.hour = hour;
        }
    }


    internal class Date
    {
        private int day;
        private int month;
        private int year;

        public Date(int day, int month, int year)
        {
            this.day = day;
            this.month = month;
            this.year = year;
        }
    }


    internal class Time
    {
        private Clock clock;
        private Date date;

        public Time(int second, int min, int hour, int day, int month, int year)
        {
            this.clock = new Clock(second, min, hour);
            this.date = new Date(day, month, year);
        }
        public Time(Clock clock, Date date)
        {
            this.clock = clock;
            this.date = date;
        }
    }
}
