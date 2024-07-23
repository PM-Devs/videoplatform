## Software Requirements Specification (SRS)

### 1. Introduction

#### 1.1 Purpose
This document specifies the software requirements for the development of a bespoke video platform for Paul Leonard. This platform will enable Paul to upload and share videos exclusively branded under his business, addressing his dissatisfaction with existing video hosting platforms.

#### 1.2 Scope
The video platform will provide functionalities for both users and administrators. Users will be able to sign up, log in, navigate video pages, and share video links. Administrators will have the ability to upload videos with titles and descriptions. The system will be a web application with a clean and intuitive user interface, ensuring seamless navigation and video playback.

#### 1.3 Definitions, Acronyms, and Abbreviations
- SRS: Software Requirements Specification
- UI: User Interface
- ER: Entity-Relationship
- Git: Version control system

#### 1.4 References
- [AmaliTech](https://www.amalitech.org)

#### 1.5 Overview
The remainder of this document includes detailed descriptions of the system functionalities, user requirements, system architecture, and other non-functional requirements. It also provides information on the deliverables, including the source code, database design, and deployment link.

### 2. General Description

#### 2.1 Product Perspective
The video platform is an independent web application designed to meet the specific needs of Paul Leonard. It is a bespoke solution tailored to provide exclusive branding for his business videos.

#### 2.2 Product Functions
- User Management: Signup, login, account verification, and password recovery.
- Video Navigation: Navigate between video pages, view video details, and control video playback.
- Video Sharing: Share video links on different platforms.
- Video Management (Admin): Upload and manage video content with titles and descriptions.

#### 2.3 User Characteristics
- **End Users**: Individuals who will sign up, log in, and view the videos.
- **Administrators**: Users with administrative privileges to upload and manage video content.

#### 2.4 Constraints
- The application must be accessible on major web browsers.
- The application must ensure secure authentication and authorization.
- Video content should be efficiently stored and streamed.

#### 2.5 Assumptions and Dependencies
- Users will have access to the internet to use the application.
- Users will have basic knowledge of navigating web applications.
- The application will be hosted on a reliable web server.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 User Registration and Authentication
- **FR1**: The system shall allow users to sign up with an email and password.
- **FR2**: The system shall send an account verification email upon signup.
- **FR3**: The system shall allow users to log in with a verified email and password.
- **FR4**: The system shall provide a feature to reset passwords.

##### 3.1.2 Video Navigation
- **FR5**: The system shall allow users to navigate between video pages.
- **FR6**: The system shall present one video per page.
- **FR7**: The system shall provide "Next" and "Previous" buttons to navigate between videos.
- **FR8**: The system shall hide the "Next" button when there are no more videos to display.
- **FR9**: The system shall hide the "Previous" button when there are no previous videos to display.
- **FR10**: The system shall provide common control buttons for video playback (play, pause, volume, etc.).

##### 3.1.3 Video Sharing
- **FR11**: The system shall provide a share button for users to share a link to the current video page.

##### 3.1.4 Video Management (Admin)
- **FR12**: The system shall allow administrators to upload videos with a title and description.
- **FR13**: The system shall display the business logo prominently at the top of each video page.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
- **NFR1**: The system should load video pages within 3 seconds.
- **NFR2**: The system should support concurrent users without performance degradation.

##### 3.2.2 Security
- **NFR3**: The system shall use HTTPS to ensure secure communication.
- **NFR4**: The system shall securely store user credentials using encryption.

##### 3.2.3 Usability
- **NFR5**: The system shall have an intuitive and user-friendly interface.
- **NFR6**: The system shall be accessible on major web browsers (Chrome, Firefox, Safari, Edge).

##### 3.2.4 Reliability
- **NFR7**: The system shall have an uptime of 99.9%.

### 4. System Architecture

#### 4.1 Database Design
The system will use a relational database to store user data, video information, and other necessary records. The ER diagram will provide a detailed structure of the database design, including tables, relationships, and key constraints.

### 5. Deliverables
- **Source Code**: The complete source code of the web application, managed in a GitHub repository with a reasonable number of commits and a well-written README file.
- **ER Diagram**: A comprehensive ER diagram illustrating the database design.
- **Deployed Link**: A link to the deployed web application.

### 6. Appendices

#### 6.1 Assumptions
- The client will provide the business logo and any specific branding guidelines.
- The client will provide feedback during the development process to ensure the final product meets their expectations.
