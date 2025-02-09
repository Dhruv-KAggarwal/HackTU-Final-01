import React, { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const [menuActive, setMenuActive] = useState(false);
  const [navbarColor, setNavbarColor] = useState('transparent');

  const handleMenuToggle = () => {
    setMenuActive(prevState => !prevState);
  };

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 300) {
        setNavbarColor("#002648");
      } else {
        setNavbarColor("transparent");
      }
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="App">
      <header>
        <nav style={{ backgroundColor: navbarColor }}>
          <div className="logo">
            <a href="index.html"><img src="/images/fav.png" alt="Logo" className="logo-img" /></a>
            <span>GeneticX</span>
          </div>
          <div className={`nav-links-container ${menuActive ? 'active' : ''}`}>
            <ul className={`nav-links ${menuActive ? 'active' : ''}`} id="nav-links">
              <li><a href="index.html">Home</a></li>
              <li><a href="#services-container">Services</a></li>
              <li><a href="#meetOurTeam">Team</a></li>
              <li><a href="#questions-container">FAQs</a></li>
              <li><a href="Login.html"><button id="register-btn">Register</button></a></li>
            </ul>
          </div>
          <div className="toggler" id="toggler" onClick={handleMenuToggle}>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </nav>
      </header>

    <section className="main">
        <video autoPlay loop muted id="background-video">
          <source src="/assets/video6.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <div className="main-content">
            <div className="text-container">
                <div className="typing">
                    <h1>DECODE YOUR DNA</h1>
                </div>
            </div> 
          <a href="http://127.0.0.1:5000"><button className="button">
            <span className="button_lg">
              <span className="button_sl"></span>
              <span className="button_text">Get Started</span>
            </span>
          </button></a>
        </div>
    </section>

    <section className="website-container">
      <h2>Upload Your <p>DNA</p> like a Pro !</h2>
      <div className="website-info">
        <div className="sub-section">
          <img src="../images/tick mark.png" alt="" />
          <p>Genetic Analysis</p>
          <div className="sub-section-content">
            <p>Upload your DNA in depth analysis.</p>
          </div>
        </div>

        <div className="sub-section">
          <img src="images/tick mark.png" alt="" />
          <p>Predict Impacts</p>
          <div className="sub-section-content">
            <p>Understood what those mutations mean for you.</p>
          </div>
        </div>

        <div className="sub-section">
          <img src="../images/tick mark.png" alt="" />
          <p>Learn Genetics</p>
          <div className="sub-section-content">
            <p>Dive into the wild <br /> world of DNA science.</p>
          </div>
        </div>
      </div>
    </section>

    <section className="info-container">
            <div className="main-info">
                <div className="main-info-card">
                    <img src="images/icon1.png" alt="" />
                    <hr />
                    <h3>500+</h3>
                    <p>DNA SAMPLES</p>
                </div>
                <div className="main-info-card">
                    <img src="images/icon2.png" alt="" />
                    <hr />
                    <h3>100+</h3>
                    <p>Mutations Identified</p>
                </div>
                <div className="main-info-card">
                    <img src="images/icon3.png" alt="" />
                    <hr />
                    <h3>50+</h3>
                    <p>Reports Generated</p>
                </div>
                <div className="main-info-card">
                    <img src="images/icon4.png" alt="" />
                    <hr />
                    <h3>10+</h3>
                    <p>Genetic Disorders</p>
                </div>
            </div>
    </section>

    <section className="services-container" id="services-container">
            <h3>Our Services</h3>
            <p>Unlock the full potential of GeneticX with exceptional features and unmatched performances.</p>
            <div className="services-subcontainer">
                <div className="services-cards-cont">
                    <div className="card">
                        <img src="../images/Services-icon1.png" alt="" />
                        <h3>DNA Analysis</h3>
                        <p>In depth examination of your genetic sequences.</p>
                    </div>
                    <div className="card responsive-card-vanish">
                        <img src="./images/Services-icon2.png" alt="" />
                        <h3>Risk Assessment</h3>
                        <p>Evaluate your susceptibility to various diseases.</p>
                    </div>
                </div>
                <div className="services-cards-cont">
                    <div className="card">
                        <img src="../images/Services-icon3.png" alt="" />
                        <h3>Mutatation Detection</h3>
                        <p>AI-powered mutation detection to access its impact.</p>
                    </div>
                    <div className="card responsive-card-vanish">
                        <img src="../images/Services-icon4.png" alt="" />
                        <h3>Personalized Reports</h3>
                        <p>Recieve detailed insights into your DNA and health risks.</p>
                    </div>
                </div>
            </div>
    </section>

    <section className="analysis-container">
            <h3>Start Analyzing your DNA</h3>
            <div className="analysis-subcontainer">
                <div className="analysis-card">
                    <img src="/images/analysis-pic1.jpeg" alt="" />
                    <h4>Free</h4>
                    <p>Easily upload your DNA sequences and let GeneticX do the magic!</p>
                     <a href="form.html"><button>Get now</button></a>
                </div>
                <div className="analysis-card">
                    <img src="/images/analysis-pic2.jpeg" alt="" />
                    <h4>Premium</h4>
                    <p>Unlock advanced features for in-depth analysis and reporting</p>
                     <a href="form.html"><button>Get now</button></a>

                </div>
            </div>
    </section>
    
    <section className="meetOurTeam" id="meetOurTeam">
            <h2>Meet our Team - <p>Dive Into Infinity</p></h2>

            <div className="team-info">
                <div className="team-cards">
                    <img src="images/Abhinav.jpg" id="lead-img" />
                    
                    <p id="name">Abhinavpreet Singh</p>
                    <p>Team Lead</p>

                    <div className="team-media">
                        <a href="" target="_blank"><i className="fa-brands fa-github"></i></a>
                        <a href="https://www.instagram.com/aps__arora/" target="_blank"><i className="bx bxl-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/abhinavpreet-singh-arora/" target="_blank"><i className="fa-brands fa-linkedin-in"></i></a>
                        <a href="https://www.x.com" target="_blank"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>

                </div>

                <div className="team-cards">
                    <img src="images/Yamini.jpg" alt="" />
                    
                    <p id="name">Yamini Baluni</p>
                    <p>UI/UX Designer</p>

                    <div className="team-media">
                        <a href="" target="_blank"><i className="fa-brands fa-github"></i></a>
                        <a href="https://www.instagram.com/_simplyyamini/" target="_blank"><i className="bx bxl-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/yamini-baluni-49985b320/" target="_blank"><i className="fa-brands fa-linkedin-in"></i></a>
                        <a href="" target="_blank"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>

                </div>

                <div className="team-cards">
                    <img src="images/Dhruv.jpg" alt="" />
                    
                    <p id="name">Dhruv K. Aggarwal</p>
                    <p>AI Specialist</p>

                    <div className="team-media">
                        <a href="" target="_blank"><i className="fa-brands fa-github"></i></a>
                        <a href="https://www.instagram.com/dka_india/" target="_blank"><i className="bx bxl-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/dhruv-kumar-aggarwal/" target="_blank"><i className="fa-brands fa-linkedin-in"></i></a>
                        <a href="" target="_blank"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>

                </div>

                <div className="team-cards">
                    <img src="images/Pratham.jpg" alt="" />
                    
                    <p id="name">Pratham Mittal</p>
                    <p>Web Developer</p>

                    <div className="team-media">
                        <a href="" target="_blank"><i className="fa-brands fa-github"></i></a>
                        <a href="https://www.instagram.com/prathammittall/" target="_blank"><i className="bx bxl-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/pratham-mittal-057420324/" target="_blank"><i className="fa-brands fa-linkedin-in"></i></a>
                        <a href="https://x.com/Prathammittalll" target="_blank"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>

                </div>
            </div>
    </section>

    <section className="questions-container" id="questions-container">
            <h3>Frequently asked questions</h3>
            <p>Here are some of the common questions people ask about us</p>
            <div className="questions-subcontainer">
                <div className="intro">
                    <h3>What is GeneticX?</h3>
                    <i className="fa-solid fa-caret-down icon-1"></i>
                </div>
                <p>GeneticX is an AI-powered platform that analyzes your DNA to detect mutations, provide personalized health insights, and helps you explore genetic risks, ancestral history, and much more.</p>

                <div className="intro">
                    <h3>How does it works ?</h3>
                    <i className="fa-solid fa-caret-down icon-1"></i>
                </div>
                <p>GeneticX is an AI-powered platform that analyzes your DNA to detect mutations, provide personalized health insights, and helps you explore genetic risks, ancestral history, and much more.</p>

                <div className="intro">
                    <h3>How accurate are the results?</h3>
                    <i className="fa-solid fa-caret-down icon-1"></i>
                </div>
                <p>GeneticX is an AI-powered platform that analyzes your DNA to detect mutations, provide personalized health insights, and helps you explore genetic risks, ancestral history, and much more.</p>

                <div className="intro">
                    <h3>What type of information will I get in my report?</h3>
                    <i className="fa-solid fa-caret-down icon-1"></i>
                </div>
                <p>GeneticX is an AI-powered platform that analyzes your DNA to detect mutations, provide personalized health insights, and helps you explore genetic risks, ancestral history, and much more.</p>
            </div>

    </section>

    <section className="last-section">
        <div className="sub-section">
            <h6>Unlock the Secrets of Your DNA</h6>
            <p>Discover insights, predict outcomes, and shape the future of genetic research.</p>
        </div>
        <a href="form.html"><button>Get Started</button></a>
    </section>

    <footer>
        <div className="footer-container">
            <div className="footer-about">
                <img src="/images/fav.png" alt="logo" />
                <h6>GeneticX</h6>
                <p id="about-para">
                    GeneticX is an AI-powered web tool where users can upload a DNA
                    Sequence and visualise potential mutations on protein structures for
                    any disease susceptibility.
                </p>
            </div>

            <div className="footer-services">
                <h6>Our Services</h6>
                <ul>
                    <li>DNA ANALYSIS</li>
                    <li>RISK ASSESSMENT</li>
                    <li>MUTATION DETECTION</li>
                    <li>PERSONALISED REPORTS</li>
                </ul>
            </div>

            <div className="footer-links">
                <h6>Quick Links</h6>
                <ul>
                    <li>About us</li>
                    <li>Privacy Policy</li>
                    <li>Support</li>
                    <li>Terms of service</li>
                </ul>
            </div>

            <div className="footer-newsletter">
                <h6>Newsletter</h6>    
                <p>Stay updated and subscribe to the GeneticX newsletter!</p>

                <input type="email" placeholder="Enter your email here" id="footer-email" />
                <button id="btn-newsletter">Subscribe</button>
            </div>
        </div>

        <div className="social-media">
            <div className="social-media-icons">
                <i className="fa-brands fa-github"></i>
                <i className="bx bxl-instagram"></i>
                <i className="fa-brands fa-linkedin-in"></i>
                <i className="fa-brands fa-x-twitter"></i>
            </div>
        </div>

        <hr />
        <p className="copyright">&copy; 2025 all rights reserved by GeneticX</p>
    </footer>

    </div>
  );
};

export default App;