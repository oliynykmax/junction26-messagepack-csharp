namespace ReviewSmoke
{
    public static class Percentage
    {
        public static decimal Calculate(int completed, int total)
        {
            return (completed / total) * 100m;
        }
    }
}
