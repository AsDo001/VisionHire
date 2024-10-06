import asyncio
from src.database.models import User, Candidate, CandidateStatus, Vacancy
from random import randint, choice
from datetime import datetime
from src.loader import oauth2, db_manager



list_of_users = [
    User(username="user1", name="John Doe", email='john.doe@example.com', hashed_password=oauth2.get_password_hash("hashed_password1")),
    User(username="user2", name="Jane Smith", email='jane.smith@example.com', hashed_password=oauth2.get_password_hash("hashed_password2")),
    User(username="user3", name="Bob Johnson", email='bob.johnson@example.com', hashed_password=oauth2.get_password_hash("hashed_password3")),
    User(username="user4", name="Alice Davis", email='alice.davis@example.com', hashed_password=oauth2.get_password_hash("hashed_password4")),
    User(username="user5", name="Charlie Brown", email='charlie.brown@example.com', hashed_password=oauth2.get_password_hash("hashed_password5")),
    User(username="user6", name="David Wilson", email='david.wilson@example.com', hashed_password=oauth2.get_password_hash("hashed_password6")),
    User(username="user7", name="Emily Davis", email='emily.davis@example.com', hashed_password=oauth2.get_password_hash("hashed_password7")),
    User(username="user8", name="Frank Martin", email='frank.martin@example.com', hashed_password=oauth2.get_password_hash("hashed_password8")),
    User(username="user9", name="Grace Lewis", email='grace.lewis@example.com', hashed_password=oauth2.get_password_hash("hashed_password9")),
    User(username="user10", name="Hannah White", email='hannah.white@example.com', hashed_password=oauth2.get_password_hash("hashed_password10")),
    User(username="user11", name="Jack Harris", email='jack.harris@example.com', hashed_password=oauth2.get_password_hash("hashed_password11")),
    User(username="user12", name="Ivy Walker", email='ivy.walker@example.com', hashed_password=oauth2.get_password_hash("hashed_password12")),
    User(username="user13", name="Kevin Scott", email='kevin.scott@example.com', hashed_password=oauth2.get_password_hash("hashed_password13")),
    User(username="user14", name="Laura Clark", email='laura.clark@example.com', hashed_password=oauth2.get_password_hash("hashed_password14")),
    User(username="user15", name="Megan Hughes", email='megan.hughes@example.com', hashed_password=oauth2.get_password_hash("hashed_password15")),
    User(username="user16", name="Nathan Brown", email='nathan.brown@example.com', hashed_password=oauth2.get_password_hash("hashed_password16")),
    User(username="user17", name="Olivia Thompson", email='olivia.thompson@example.com', hashed_password=oauth2.get_password_hash("hashed_password17")),
    User(username="user18", name="Peter Martinez", email='peter.martinez@example.com', hashed_password=oauth2.get_password_hash("hashed_password18")),
    User(username="user19", name="Quincy Robinson", email='quincy.robinson@example.com', hashed_password=oauth2.get_password_hash("hashed_password19")),
    User(username="user20", name="Rachel Lee", email='rachel.lee@example.com', hashed_password=oauth2.get_password_hash("hashed_password20")),
    User(username="user21", name="Steve Harris", email='steve.harris@example.com', hashed_password=oauth2.get_password_hash("hashed_password21")),
    User(username="user22", name="Tina Clark", email='tina.clark@example.com', hashed_password=oauth2.get_password_hash("hashed_password22")),
    User(username="user23", name="Uma Patel", email='uma.patel@example.com', hashed_password=oauth2.get_password_hash("hashed_password23")),
    User(username="user24", name="Victor Gonzalez", email='victor.gonzalez@example.com', hashed_PASSWORD=oauth2.get_password_hash("hashed_password24")),
    User(username="user25", name="Wendy Adams", email='wendy.adams@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password25")),
    User(username="user26", name="Xander Brooks", email='xander.brooks@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password26")),
    User(username="user27", name="Yara Fletcher", email='yara.fletcher@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password27")),
    User(username="user28", name="Zane Moore", email='zane.moore@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password28")),
    User(username="user29", name="Abby Phillips", email='abby.phillips@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password29")),
    User(username="user30", name="Blake Sanders", email='blake.sanders@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password30")),
    User(username="user31", name="Carl Bennett", email='carl.bennett@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password31")),
    User(username="user32", name="Dana Porter", email='dana.porter@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password32")),
    User(username="user33", name="Eli Perry", email='eli.perry@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password33")),
    User(username="user34", name="Fiona Cooper", email='fiona.cooper@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password34")),
    User(username="user35", name="George Mitchell", email='george.mitchell@example.com', hashed_PASSWORD=oauth2.get_passowrd_hash("hashed_password35"))
]



list_of_candidates = [
 Candidate(
  first_name="John",
  family_name="Doe",
  surname="Smith",
  phone="123-456-7890",
  email="john.doe@example.com",
  city="New York",
  vacancy_id=1,
  resume_file="john_doe_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="Jane",
  family_name="Roe",
  surname="Johnson",
  phone="987-654-3210",
  email="jane.roe@example.com",
  city="San Francisco",
  vacancy_id=2,
  resume_file="jane_roe_resume.pdf",
  status=CandidateStatus.interview
 ),
 Candidate(
  first_name="Alice",
  family_name="Smith",
  surname="Brown",
  phone="555-123-4567",
  email="alice.smith@example.com",
  city="Chicago",
  vacancy_id=3,
  resume_file="alice_smith_resume.pdf",
  status=CandidateStatus.hired
 ),
 Candidate(
  first_name="Robert",
  family_name="Johnson",
  surname="Williams",
  phone="111-222-3333",
  email="robert.johnson@example.com",
  city="Los Angeles",
  vacancy_id=4,
  resume_file="robert_johnson_resume.pdf",
  status=CandidateStatus.rejected
 ),
 Candidate(
  first_name="Emily",
  family_name="Taylor",
  surname="Davis",
  phone="444-555-6666",
  email="emily.taylor@example.com",
  city="Austin",
  vacancy_id=5,
  resume_file="emily_taylor_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="John",
  family_name="Doe",
  surname="Smith",
  phone="123-456-7890",
  email="john.doe@example.com",
  city="New York",
  vacancy_id=1,
  resume_file="john_doe_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="Jane",
  family_name="Roe",
  surname="Johnson",
  phone="987-654-3210",
  email="jane.roe@example.com",
  city="San Francisco",
  vacancy_id=2,
  resume_file="jane_roe_resume.pdf",
  status=CandidateStatus.interview
 ),
 Candidate(
  first_name="Alice",
  family_name="Smith",
  surname="Brown",
  phone="555-123-4567",
  email="alice.smith@example.com",
  city="Chicago",
  vacancy_id=3,
  resume_file="alice_smith_resume.pdf",
  status=CandidateStatus.hired
 ),
 Candidate(
  first_name="Robert",
  family_name="Johnson",
  surname="Williams",
  phone="111-222-3333",
  email="robert.johnson@example.com",
  city="Los Angeles",
  vacancy_id=4,
  resume_file="robert_johnson_resume.pdf",
  status=CandidateStatus.rejected
 ),
 Candidate(
  first_name="Emily",
  family_name="Taylor",
  surname="Davis",
  phone="444-555-6666",
  email="emily.taylor@example.com",
  city="Austin",
  vacancy_id=5,
  resume_file="emily_taylor_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="Michael",
  family_name="Brown",
  surname="Garcia",
  phone="777-888-9999",
  email="michael.brown@example.com",
  city="Seattle",
  vacancy_id=6,
  resume_file="michael_brown_resume.pdf",
  status=CandidateStatus.interview
 ),
 Candidate(
  first_name="Sarah",
  family_name="Wilson",
  surname="Martinez",
  phone="222-333-4444",
  email="sarah.wilson@example.com",
  city="Miami",
  vacancy_id=7,
  resume_file="sarah_wilson_resume.pdf",
  status=CandidateStatus.hired
 ),
 Candidate(
  first_name="David",
  family_name="Lopez",
  surname="Walker",
  phone="888-999-0000",
  email="david.lopez@example.com",
  city="Denver",
  vacancy_id=8,
  resume_file="david_lopez_resume.pdf",
  status=CandidateStatus.rejected
 ),
 Candidate(
  first_name="Jessica",
  family_name="Lee",
  surname="Hall",
  phone="333-444-5555",
  email="jessica.lee@example.com",
  city="Boston",
  vacancy_id=9,
  resume_file="jessica_lee_resume.pdf",
  status=CandidateStatus.interview
 ),
 Candidate(
  first_name="James",
  family_name="Green",
  surname="Harris",
  phone="666-777-8888",
  email="james.green@example.com",
  city="Detroit",
  vacancy_id=10,
  resume_file="james_green_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="Sophia",
  family_name="Clark",
  surname="Young",
  phone="101-202-3030",
  email="sophia.clark@example.com",
  city="Phoenix",
  vacancy_id=11,
  resume_file="sophia_clark_resume.pdf",
  status=CandidateStatus.hired
 ),
 Candidate(
  first_name="Liam",
  family_name="King",
  surname="Wright",
  phone="404-505-6060",
  email="liam.king@example.com",
  city="Philadelphia",
  vacancy_id=12,
  resume_file="liam_king_resume.pdf",
  status=CandidateStatus.rejected
 ),
 Candidate(
  first_name="Olivia",
  family_name="Scott",
  surname="Torres",
  phone="707-808-9090",
  email="olivia.scott@example.com",
  city="San Antonio",
  vacancy_id=13,
  resume_file="olivia_scott_resume.pdf",
  status=CandidateStatus.interview
 ),
 Candidate(
  first_name="Noah",
  family_name="Adams",
  surname="Nguyen",
  phone="010-121-3141",
  email="noah.adams@example.com",
  city="San Diego",
  vacancy_id=14,
  resume_file="noah_adams_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="Emma",
  family_name="Nelson",
  surname="Hill",
  phone="151-617-1819",
  email="emma.nelson@example.com",
  city="Dallas",
  vacancy_id=15,
  resume_file="emma_nelson_resume.pdf",
  status=CandidateStatus.hired
 ),
 Candidate(
  first_name="William",
  family_name="Parker",
  surname="Collins",
  phone="212-223-2425",
  email="william.parker@example.com",
  city="San Jose",
  vacancy_id=16,
  resume_file="william_parker_resume.pdf",
  status=CandidateStatus.rejected
 ),
 Candidate(
  first_name="Ava",
  family_name="Mitchell",
  surname="Turner",
  phone="262-728-2930",
  email="ava.mitchell@example.com",
  city="Austin",
  vacancy_id=17,
  resume_file="ava_mitchell_resume.pdf",
  status=CandidateStatus.interview
 ),
 Candidate(
  first_name="James",
  family_name="Martinez",
  surname="Carter",
  phone="313-335-3637",
  email="james.martinez@example.com",
  city="Jacksonville",
  vacancy_id=18,
  resume_file="james_martinez_resume.pdf",
  status=CandidateStatus.expected
 ),
 Candidate(
  first_name="Isabella",
  family_name="Roberts",
  surname="Phillips",
  phone="404-849-5051",
  email="isabella.roberts@example.com",
  city="Fort Worth",
  vacancy_id=19,
  resume_file="isabella_roberts_resume.pdf",
  status=CandidateStatus.hired
 ),
]

list_of_vacancies = [
Vacancy(
  title="Software Engineer",
  description="We are looking for an experienced Software Engineer.",
  location="New York",
  creator_username="recruiter123",
  created_at=datetime.now(), 
  status=True
),
Vacancy(
    title="System Administrator",
    description="System Administrator with Linux experience required.",
    location="Dallas",
    creator_username="sysadmin_expert",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Embedded Systems Engineer",
    description="Engineer needed for development of embedded systems.",
    location="San Diego",
    creator_username="embedded_eng",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Cloud Solutions Architect",
    description="Cloud Solutions Architect needed for AWS and Azure platforms.",
    location="Denver",
    creator_username="cloud_architect",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Cybersecurity Specialist",
    description="Specialist needed for cybersecurity risk assessments.",
    location="Phoenix",
    creator_username="cybersec_specialist",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Mobile Application Developer",
    description="Developer needed for Android and iOS application development.",
    location="Portland",
    creator_username="mobile_dev",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="AI Research Scientist",
    description="Research Scientist needed with focus on artificial intelligence.",
    location="Toronto",
    creator_username="ai_scientist",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="IT Support Specialist",
    description="Support Specialist needed for troubleshooting IT issues.",
    location="Philadelphia",
    creator_username="it_support",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="SEO Specialist",
    description="SEO Specialist required to improve search engine rankings.",
    location="Boston",
    creator_username="seo_expert",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Database Administrator",
    description="Administrator required for MySQL and PostgreSQL databases.",
    location="San Jose",
    creator_username="db_admin",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Blockchain Developer",
    description="Developer needed for blockchain and cryptocurrency projects.",
    location="Las Vegas",
    creator_username="blockchain_dev",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Technical Writer",
    description="Technical Writer needed for creating manuals and guides.",
    location="Washington D.C.",
    creator_username="tech_writer",
    created_at=datetime.now(),
    status=True
  ),
  Vacancy(
    title="Salesforce Developer",
    description="Salesforce Developer with Lightning experience required.",
    location="Houston",
    creator_username="salesforce_dev",
    created_at=datetime.now(),
    status=True
  )
]

async def fill():
    async with db_manager.get_session() as session:
        result = await session.add_all(list_of_users)
        return result.scalar()
 

asyncio.run(fill())
# list_of_users = [ User( username = ''.join([chr(randint(ord('a'), ord('z'))) for i in range(randint(4, 10))]), email = ''.join([chr(randint(ord('a'), ord('z'))) for i in range(randint(4, 10))])+'@example.com', hashed_password = ''.join([chr(randint(ord('a'), ord('z'))) for i in range(30)]), role = choice([Role.RECURITER, Role.HR])) for i in range(1000) ]