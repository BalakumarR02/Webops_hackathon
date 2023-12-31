#1/usr/bin/python3

# Import required libraries 
import webbrowser
import urllib.parse

# The global tag set
tag_set = {
    "GraphQL",
    "Data Structures and Algorithms",
    "HTML",
    "MERN",
    "Blockchain",
    "Full stack development",
    "Frontend development",
    "Backend development",
    "Database management",
    "App development",
    "NFTs",
    "Cryptocurrency",
    "Mining",
    "Encryption",
    "Web designing",
    "Cloud computing",
    "Web 3.0",
    "DevOps lifecycle",
    "Software Testing",
    "Version Control",
    "Web Architectures",
    "Agile Practices",
    "System Design",
    "Team-Sahaay",
    "Sahaay",
    "Social-innovation-club",
    "Social-innovation",
    "Social-impact",
    "Innovation",
    "Technology",
    "Society",
    "Design-thinking",
    "Design-process",
    "Product-development",
    "Rural-tech",
    "Sustainability",
    "Assistive-devices",
    "Agri-tech",
    "Sanitation",
    "3D-modeling",
    "Fusion-360",
    "Mechanical-design",
    "Arduino",
    "IOT",
    "Robotics",
    "Electronics",
    "Machine learning",
    "Image processing",
    "Programming",
    "PC",
    "Optimization",
    "Time-complexity",
    "Efficiency",
    "Codeforces",
    "Codechef",
    "Atcoder",
    "Leetcode",
    "Coding",
    "Competitive-programming",
    "Ratings",
    "Dynamic-programming",
    "Graphs",
    "C++",
    "Contest",
    "Digital Design",
    "FPGAs",
    "MCU and SoCs",
    "Displays",
    "Camera modules",
    "Signal processing",
    "SDR",
    "HackerArt",
    "TinyML",
    "Parallel processing",
    "RTOS",
    "Embedded Systems",
    "GPUs",
    "Power Electronics",
    "analytics",
    "classification",
    "regression",
    "segmentation",
    "detection",
    "recognition",
    "object-detection",
    "synthesis",
    "generation",
    "translation",
    "distillation",
    "visualization",
    "eda",
    "language-modelling",
    "cnn",
    "Product",
    "Design",
    "Entrepreneurship",
    "Marketing",
    "Sketching",
    "Start-up",
    "Business-idea",
    "Product-teardown",
    "Aesthtic-design",
    "Sales",
    "Pitching",
    "3D-Printing",
    "CAD",
    "User-Interface",
    "User-experience",
    "Market-research",
    "User-research",
    "Industrial sketching",
    "Business",
    "Product-thinking",
    "Manufacturing",
    "Patent",
    "Customer-research",
    "Product-Management",
    "rnn",
    "generative-adversarial-networks",
    "gan",
    "attention",
    "transformers",
    "bert",
    "hpc",
    "pytorch",
    "sklearn",
    "tensorflow",
    "keras",
    "Genetic-Engineering",
    "Synthetic-Biology",
    "Direted-Evolution",
    "Cloning",
    "numpy",
    "Transformation",
    "Enzyme",
    "Bacterial+Cellulose",
    "lactose",
    "targeted-tumor-therapy",
    "Cytosine-deaminase",
    "insulin",
    "wound-healing",
    "biocompatible",
    "Flourouracil",
    "enzyme-prodrug+therapy",
    "Yeast",
    "K.xylinus",
    "iBot",
    "robotics",
    "automation",
    "computer-vision",
    "reinforcement-learning",
    "NLP",
    "ROS",
    "navigation",
    "gazebo",
    "ansys",
    "actuators",
    "manipulators",
    "inverse-kinematics",
    "gears",
    "matlab",
    "differential-kinematics",
    "motors",
    "microcontrollers",
    "sensors",
    "raspberry-pi",
    "iot",
    "communication-protocol",
    "PMSM & SPWM control",
    "PCB",
    "Python",
    "Unity",
    "Blender",
    "Techno entertainment",
    "Kinect",
    "AR",
    "VR",
    "GameDev",
    "Game Development",
    "GameDev Community",
    "Games",
    "AI",
    "Entertainment",
    "CVI",
    "Artificial-Intelligence",
    "Deep-Learning",
    "Computer-Vision",
    "Natural-Language-Processing",
    "Reinforcement-Learning",
    "Data-Science",
    "Image-Processing",
    "Image-Classification",
    "Neural-Networks",
    "Linear-Regression",
    "pandas",
    "LIGO",
    "Astronomy",
    "Blackhole",
    "Gravity",
    "Relativity",
    "Gravitational waves",
    "Physics",
    "Neutron Star",
    "Quasar",
    "Galaxy",
    "Rocket",
    "Satellite",
    "Spacecraft",
    "Particle",
    "CERN",
    "Particle Accelerator",
    "Star",
    "Red Giant",
    "White dwarf",
    "Planet",
    "Boson",
    "Lepton",
    "Quark",
    "Orbit",
    "Binary Star",
    "Supernova",
    "Hypernova",
    "Space",
    "Time",
    "Astronaut",
    "Nuclear Force",
    "Constellation",
    "Equator",
    "Comet",
    "Asteroid",
    "Coordinate System",
    "Telescope",
    "James Webb Telescopoe",
    "Horizon",
    "Hubble Telescope",
    "Sun",
    "Parker Probe",
    "MOM (Mars Orbiter Mission)",
    "Orion",
    "Pole Star",
    "sql",
    "opencv",
    "Slicer",
    "G-code",
    "Marlin",
    "Printing material",
    "Innovations",
    "Extruder",
    "Food Printing",
    "Cooling fan",
    "Print bed",
    "FDM",
    "Microcontroller",
    "Frame",
}

# The global club set
club_set = {
    "3D Printing Club",
    "Aero Club",
    "AI Club (Analytics/CVI)",
    "Biotech Club",
    "Electronics Club",
    "Horizon",
    "iBot Club",
    "Maths Club",
    "Product Design Club",
    "Programming Club",
    "Team Envisage",
    "Team Sahaay",
    "WebOps and Blockchain Club",
}

# Base URL
url = 'https://cfi.iitm.ac.in/blog'

# Input queries
blog_search = input("Enter the CFI blog search query:")
tag_filter = input("Enter the tag filers separated by commas:")
club_filter = input("Enter the club filers separated by commas:")

# Prepare URL parameters
params = []

# Check if a blog search query was provided
if blog_search:
    # If blog_search is not an empty string, add it to the URL parameters after URL encoding
    params.append(f'search={urllib.parse.quote(blog_search)}')

# Check if tag filters were provided
if tag_filter:
    # Split tag_filter into individual queries based on commas and create a set of matching tags
    tag_query = {tag for query in tag_filter.split(',') for tag in tag_set if query.lower() in tag.lower()}
    
    # Check if there are matching tags
    if tag_query:
        # Add matching tags to the URL parameters after URL encoding
        params.append(f'tag={",".join(urllib.parse.quote(tag) for tag in tag_query)}')

# Check if club filters were provided
if club_filter:
    # Split club_filter into individual queries based on commas and create a set of matching clubs
    club_query = {club for query in club_filter.split(',') for club in club_set if query.lower() in club.lower()}
    
    # Check if there are matching clubs
    if club_query:
        # Add matching clubs to the URL parameters after URL encoding
        params.append(f'club={",".join(urllib.parse.quote(club) for club in club_query)}')

# Construct the final URL
if params:
    url += '?' + '&'.join(params)

try:
    # Attempt to open the specified URL in the default web browser
    webbrowser.open(url)

except Exception as error:
    # If an exception occurs during the attempt to open the URL, catch it and handle it gracefully
    print(f"An error occurred: {error}")