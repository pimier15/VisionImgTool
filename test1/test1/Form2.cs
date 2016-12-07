using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace test1
{
    public delegate void PassPanelShowClick();
    public partial class Form2 : Form
    {
        public event PassPanelShowClick evtPanelShow;
        private void button1_Click( object sender , EventArgs e )
        {
            evtPanelShow();
        }

        public Form2()
        {
            InitializeComponent();
        }
    }
}
