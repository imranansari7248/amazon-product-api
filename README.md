<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/imranansari72/amazon-product-api">
    <h1>amazon-product-api</h1>
  </a>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://amazon-product-apis.herokuapp.com/api?query=iphone)

Its a simple api for fetching product details of amazon e-commerse website. Fetch amazon product and use them in your app and wherever you want.

Give your support and also suggest changes by forking this repo and creating a pull request or opening an issue.


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [node.js](https://nodejs.org/)
* [express.js](https://expressjs.com/)
* [python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can make a local environment or use my deployed app.

https://amazon-product-apis.herokuapp.com/

### Prerequisites

Should have python and nodejs localy install.

### Installation

Install app to use in your local environment.

1. Clone the repo
   ```sh
   git clone https://github.com/imranansari72/amazon-product-api
   cd amazon-product-api
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. change directory
   ```sh
    node app.js
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

end-point : https://amazon-product-apis.herokuapp.com/

OR

If you are using localhost : 
```link
http://localhost:3000/
```
For checking api is live visit : <-endpoint->/api   

/api 
 queries parrameters :
 1. query (required) : 
 ```link 
 https://amazon-product-apis.herokuapp.com/api?query=laptop
 ```
 2. price (can be range or number) (optional) :
 ```link
 https://amazon-product-apis.herokuapp.com/api?query=laptop&price=50000-60000
 https://amazon-product-apis.herokuapp.com/api?query=laptop&price=50000
 ```
 3. brand (optional) :
 ```link
 https://amazon-product-apis.herokuapp.com/api?query=laptop&price=50000-60000&brand=dell
 ```
 4. for fetching more results for same request please add page parameter :
 ```link
 https://amazon-product-apis.herokuapp.com/api?query=laptop&price=50000-60000&page=2
 ```

/link 
 queries parrameters :
 only takes link parameter (required) :
 1.link : 
 ```link
 https://amazon-product-apis.herokuapp.com/link?link=<link-of-product>
 ```

Enjoy the api.

_please refer to the [help](https://amazon-product-apis.herokuapp.com/help)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request.

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Imran Ansari - [telegram](https://t.me/imranansari7248) - imranansari7248@gmail.com

Project Link: [https://github.com/imranansari72/amazon-product-api](https://github.com/imranansari72/amazon-product-api)

<p align="right">(<a href="#top">back to top</a>)</p>

[product-screenshot]: images/screenshot.png