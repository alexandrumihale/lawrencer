# Lawrencer: an expense tracker for Bolt trips

## DISCLAIMER

This script is <b>not</b> an official Bolt application and it is in no way associated with Bolt, Bolt Romania, Bolt Technology or OÜ (Estonia) and it is intented to be used for demonstration/portfolio purposes.

Feel free to use this script at your own discretion.

## Table of Contents

- [About](#about)
- [Usage](#usage)

## About <a name = "about"></a>

Lawrencer is a proof of concept destined for individuals that use Bolt (the ridesharing app) for professional purposes and receive refunds from their employer.

Please note that it was tested exclusively with Bolt invoices generated in Romania, the entire script being destined for Romania-based employees.

### Prerequisites

In order to work properly, make sure you have the latest version of Python, along with the latest version of pip.
Moreover, two libraries were used for this script: PyPDF2 and openpyxl.

For pip and the libraries, use these commands in your terminal/command prompt.

<pre>
  <code>
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip install PyPDF2
    pip install openpyxl
  </code>
</pre>

## Usage <a name = "usage"></a>

<ol>
<li>Download/clone the repository.</li>
<li>Place your PDF invoices in the same folder/directory. </li>
<li>Run app.py.</li>
<li>Enter your name and your expense code or explanation.</li>
</ol>