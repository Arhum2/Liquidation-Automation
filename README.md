
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Arhum2/Manifest-Scrapper">
    <img src="https://user-images.githubusercontent.com/82200170/183231685-baf5e7c1-6d57-4c4d-9aa8-bba81d35b7d3.png">
  </a>

  <h3 align="center">Liquidity services manifest web scrapper</h3>

  <p align="center">
    By Arhum Shahzad
    <br />
    <br />
    <a>This project takes manifests from Liquidity Services and uses Python and Slenium to scrape and look up items for auction. searching for items in a manifest, making it faster to source products and record data Improved product research and data compiling from 15 minutes to 1 minute per manifest. 


</a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/Arhum2/Manifest-Scrapper/issues">Report Bug</a>
    ·
    <a href="https://github.com/Arhum2/Manifest-Scrapper/pulls">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Image-1](https://user-images.githubusercontent.com/82200170/188043942-de4e5a6d-9d2d-41b4-9a2a-12a8f6d65d6b.jpg)

After sourcings furniture from [Liquadation.com](https://www.liquidation.com/index?gclid=CjwKCAjwnrjrBRAMEiwAXsCc40uSxzQCMHP_9XwiY_rmfUpJ4WB1EDi4zOMVMNMTv_jmsZp39XRB5xoCpfIQAvD_BwE)  I realized most of my time was consumed manually by looking up and researching products in a manifest. After spending some time learning Python automation I expanded my knowledge to this project. Manifest Scrapper parses through a .csv file and looks up each product listed in a Liquidity Services manifest.


### Here's why I created this project:
* Improved product research and data compiling allowing for less time to be iinvested with the same return
* You shouldn't be doing the same tasks over and over
* implements DRY principles to my business

### Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)

### Prerequisites

1. Install [Python](https://www.python.org/)
2. Install [Selenium](https://www.selenium.dev/)
3. Check your Chrome version and download your [Chrome driver](https://chromedriver.chromium.org/downloads)

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/Arhum2/Manifest-Scrapper.git
   ```
2. Change `PATH` in manifest.py to your chromedriver.exe file path
   ```sh
   PATH = 'ENTER chromedriver.exe FILE PATH HERE'
   ```
3. Change line 1 in manifest.bat to your manifest.py file path
   ```js
   @py C:\FILE_PATH\manifest.py %*
   ``` <p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Here is a full demo of Manifest Scrapper taking in user input (the name of the manisfest file) and rapidly looking up each product. 


https://user-images.githubusercontent.com/82200170/187813623-06efb504-6ee3-4f81-b96d-9f58791b8004.mp4 
<p align="right">(<a href="#readme-top">back to top</a>) </p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information. <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Email - Arhumshahzad2003@gmail.com <p align="right">(<a href="#readme-top">back to top</a>)</p>
