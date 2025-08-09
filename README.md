# QA Lead Assignment - Profile Picture Upload System

A comprehensive web application demonstrating user authentication and profile picture upload functionality with automated testing using BDD (Behavior Driven Development) and Selenium.

## 🚀 Features

- **User Authentication System**
  - User registration and login functionality
  - Secure session management
  - Logout capability

- **Profile Picture Upload**
  - File size validation (max 5MB)
  - Real-time upload feedback
  - Success/error message handling

- **Modern UI/UX**
  - Clean, responsive design
  - Intuitive user interface
  - Professional styling with CSS

## 🏗️ Project Structure

```
qa_lead_assignment/
├── features/                          # BDD feature files
│   ├── profile_upload.feature        # Profile upload test scenarios
│   └── steps/                        # Step definitions
│       └── profile_upload_steps.py   # Python step implementations
├── Indee.tv-Assignment/              # Assignment-specific files
├── resources/                        # Test resources
│   ├── large-image.jpeg             # Large image for testing (>5MB)
│   └── small-image.jpeg             # Small image for testing (<5MB)
├── qa-lead-assignment-homepage.html  # Main application interface
├── run_server.py                     # Local development server
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python HTTP Server
- **Testing Framework**: Behave (BDD)
- **Web Automation**: Selenium WebDriver
- **Browser Management**: WebDriver Manager

## 📋 Prerequisites

- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Git (for version control)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ajithrao2509/Indee.tv-Assignment.git
cd qa_lead_assignment
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python run_server.py
```

The application will be available at: **http://localhost:8080**

### 4. Access the Application

Open your web browser and navigate to:
```
http://localhost:8080/qa-lead-assignment-homepage.html
```

## 🧪 Running Tests

### Execute BDD Tests

```bash
behave features/
```

### Test Scenarios

The application includes comprehensive test scenarios for profile picture upload validation:

- **File Size Validation**: Tests upload success/failure based on 5MB file size limit
- **User Registration**: Tests new user signup process
- **User Authentication**: Tests login/logout functionality
- **Upload Feedback**: Tests success and error message display

## 📱 Usage Guide

### 1. User Registration
- Enter a username and password
- Click "Sign Up" to create a new account

### 2. User Login
- Enter your registered credentials
- Click "Login" to access your profile

### 3. Profile Picture Upload
- Once logged in, you'll see the profile section
- Click "Choose File" to select an image
- Supported formats: JPEG, PNG, GIF
- Maximum file size: 5MB
- Click "Upload" to process the image

### 4. Logout
- Click the "Logout" button to end your session

## 🔧 Development

### Local Development Server

The `run_server.py` script provides a simple HTTP server for local development:

- **Port**: 8080
- **Directory**: Current working directory
- **Stop Server**: Press `Ctrl+C` in the terminal

### Adding New Features

1. Update the HTML file with new UI elements
2. Add corresponding JavaScript functionality
3. Create BDD feature files for new test scenarios
4. Implement step definitions in Python

## 🧪 Testing Strategy

### BDD Approach
- **Feature Files**: Written in Gherkin syntax for non-technical stakeholders
- **Step Definitions**: Python implementations of test steps
- **Test Scenarios**: Covering both positive and negative test cases

### Test Coverage
- User registration and authentication
- File upload validation
- Error handling and user feedback
- UI responsiveness and functionality

## 📁 File Descriptions

- **`qa-lead-assignment-homepage.html`**: Main application interface with authentication and upload functionality
- **`features/profile_upload.feature`**: BDD test scenarios for profile upload validation
- **`run_server.py`**: Simple HTTP server for local development
- **`requirements.txt`**: Python package dependencies
- **`resources/`**: Test images for validation testing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of the QA Lead Assignment and is intended for educational and demonstration purposes.

## 👨‍💻 Author

**Ajith Rao**
- GitHub: [@ajithrao2509](https://github.com/ajithrao2509)

## 🆘 Support

If you encounter any issues or have questions:

1. Check the existing issues in the repository
2. Create a new issue with detailed description
3. Include steps to reproduce the problem
4. Provide system information and error logs

---

**Happy Testing! 🧪✨**
