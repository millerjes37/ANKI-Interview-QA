import genanki

# Define a model (card template)
my_model = genanki.Model(
    1607392319,
    'Interview Questions Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

# Create a deck
my_deck = genanki.Deck(
    2059400110,
    'Interview Questions Deck')

# List of tailored interview questions and answers
questions_answers = [
    ('Tell me about yourself.', 'Hello, my name is Jackson Miller. I recently graduated with a BA in Political Science and a minor in Psychology from Wabash College. Throughout my academic and professional journey, I have developed a strong foundation in policy analysis, strategic communication, and stakeholder engagement, which I am eager to apply in a dynamic work environment. Currently, I am the Public Relations and Marketing Manager at Kroger Gardis and Regas LLP. In this role, I have successfully developed and executed comprehensive communication strategies that significantly enhanced our firms public and digital media presence. One of my proudest achievements was coordinating with board members and media stakeholders to align our messaging with organizational goals, particularly in legislative and educational initiatives. Additionally, I managed our WordPress-based website, ensuring it effectively represented our brand and facilitated user engagement. Prior to this, I served as a Summer Law Clerk and CIBE Consultant at the same firm. This experience allowed me to deeply immerse myself in the world of policy-making and stakeholder engagement. I led internal meetings on regulatory relief, met with legislators, and drafted policy documents that addressed critical issues like mental health facilities in schools. These tasks required not only a thorough understanding of the policy landscape but also the ability to communicate complex ideas clearly and persuasively. During my time at Wabash College, I interned with the Advancement Office, where I played a key role in organizing and running events focused on the stewardship of gifts. Our efforts during two days of giving resulted in raising over $3 million, which was a testament to our team’s dedication and strategic planning. Additionally, I actively engaged with students, faculty, and alumni to solicit donations, demonstrating my ability to build and maintain relationships with diverse groups. Beyond my professional roles, I am the founder of Civitas Limited, a startup in its seed phase that leverages advancements in language models to create a comprehensive stakeholder management system. This venture reflects my passion for using technology to streamline and enhance government affairs, making it more accessible and efficient. In terms of technical skills, I am proficient in R, Python, and various data analysis tools. My GitHub portfolio showcases a range of projects that I have containerized for ease of deployment, illustrating my commitment to continuous learning and practical application of my skills. Moreover, my involvement in Phi Delta Theta fraternity, where I served as Vice President, Rush Chairmen, and Risk Manager, has honed my leadership and project management abilities. I successfully managed a $30,000 budget, increased professional development opportunities by 400%, and advocated for enhanced mental health facilities on campus. My career aspirations revolve around making a significant impact in the field of public policy. I am passionate about addressing complex societal issues through innovative solutions and collaborative efforts. I believe that my diverse experiences, coupled with my strategic and analytical mindset, make me a strong candidate for roles that require both creativity and rigor. Thank you for the opportunity to introduce myself. I am excited about the prospect of contributing to your team and working together to achieve meaningful outcomes.'),
    ('What are your strengths and weaknesses?', 'One of my key strengths is my ability to engage stakeholders and create shared meaning in advocacy, as demonstrated by my work in public relations and policy drafting. I excel in strategic communication and project management, managing long-term projects while handling day-to-day tasks effectively. A weakness I am working on is delegating tasks; I tend to take on too much responsibility myself. However, I am learning to trust my team more and delegate tasks to ensure better efficiency.'),
    ('Why do you want to work here?', 'I am drawn to your organization because of its commitment to impactful policy initiatives and community engagement, which align with my passion for advocacy and strategic communication. I am impressed by your recent legislative efforts and believe my background in policy analysis and stakeholder engagement can contribute significantly to your ongoing projects.'),
    ('What are your career goals?', 'My long-term career goal is to influence public policy and drive positive change through strategic communication and stakeholder management. I aim to continue developing my skills in policy advocacy and analysis, eventually taking on leadership roles where I can shape policy and advocate for meaningful legislation.'),
    ('Can you describe a challenging situation and how you handled it?', 'During my tenure as a Summer Law Clerk at Kroger Gardis and Regas LLP, I led the regulatory relief subcommittee, which involved coordinating with various stakeholders and legislators, including Senator Crider, to address access to mental health facilities in schools. The challenge was aligning diverse viewpoints and interests. I facilitated several meetings, drafted relevant policies, and ensured all parties were heard, which resulted in a collaborative approach and successful policy recommendations.'),
    ('Why should we hire you?', 'You should hire me because I bring a unique combination of analytical prowess and strong communication skills. My experience in policy analysis, strategic communication, and stakeholder engagement has prepared me to contribute effectively to your team. Additionally, my proactive approach and proven track record in managing complex projects make me a valuable asset for achieving your organizational goals.'),
    ('What do you know about our company?', 'I know that your company is a leader in [specific field], committed to [mention specific values or recent achievements]. I admire your focus on [specific aspects relevant to your experience, such as community engagement, policy advocacy, etc.], which aligns with my professional background and career aspirations.'),
    ('Describe a time when you worked in a team.', 'At Wabash College, I was part of the advancement team that organized stewardship events, including two days of giving that raised over $3 million. I worked closely with students, faculty, and alumni, coordinating volunteers and ensuring smooth event execution. This experience taught me the importance of teamwork, communication, and effective project management.'),
    ('How do you handle stress and pressure?', 'I handle stress and pressure by staying organized and maintaining a clear focus on priorities. During my role as Public Relations and Marketing Manager at Kroger Gardis and Regas LLP, I often managed multiple projects simultaneously. I used tools like project management software and regular check-ins to stay on track. Additionally, I ensure to take short breaks and practice mindfulness techniques to keep stress levels manageable.'),
    ('What are your salary expectations?', 'Based on my research and understanding of the industry standards, I expect a salary in the range of $[specific range], which I believe reflects my skills, experience, and the value I can bring to your organization. However, I am open to discussing this further based on the overall compensation package and growth opportunities.'),
    ('How do you prioritize your work?', 'I prioritize my work by assessing the urgency and importance of each task. I use tools like to-do lists and project management software to keep track of deadlines and ensure that I allocate sufficient time to high-priority tasks. Regular reviews of my workload help me stay organized and focused.'),
    ('Describe a time when you had to solve a complex problem.', 'While working on a project at Kroger Gardis and Regas LLP, I encountered a regulatory challenge that required in-depth analysis and coordination with multiple stakeholders. I conducted thorough research, consulted with experts, and developed a comprehensive strategy that addressed the regulatory requirements and achieved the project goals. This experience reinforced my problem-solving skills and my ability to navigate complex issues.'),
    ('How do you handle feedback?', 'I view feedback as an opportunity for growth and improvement. I actively seek feedback from colleagues and supervisors to understand areas where I can enhance my performance. I listen carefully, ask clarifying questions if needed, and implement the feedback to improve my skills and work outcomes.'),
    ('Can you give an example of a time you showed leadership?', 'As Vice President of Phi Delta Theta Indiana Beta, I led initiatives that increased professional development opportunities for members by 400% and enhanced alumni engagement. I managed a $30,000 budget and coordinated with campus leadership to advocate for mental health facilities. This role allowed me to develop and demonstrate my leadership and strategic planning abilities.'),
    ('What motivates you?', 'I am motivated by the opportunity to make a positive impact through my work. The ability to influence public policy and advocate for meaningful change drives me to continuously improve my skills and take on new challenges. I am also motivated by the success of my team and the satisfaction of achieving our collective goals.'),
    ('How do you stay informed about current political events and trends?', 'I stay informed by regularly reading news from reputable sources, following key political analysts and thought leaders on social media, and participating in professional organizations and conferences. Additionally, I subscribe to policy journals and newsletters to keep up with the latest developments and trends in the political landscape.'),
    ('Describe your experience with policy analysis.', 'My experience with policy analysis includes conducting thorough research, evaluating the impact of existing policies, and drafting policy briefs and memos. At Kroger Gardis and Regas LLP, I summarized relevant news and policy solutions, drafted memos for the education team, and engaged with stakeholders to develop effective policy recommendations.'),
    ('Can you give an example of a policy you analyzed and your findings?', 'I analyzed a policy regarding access to mental health facilities in schools and presented my findings to legislators, including Senator Crider. My analysis highlighted the benefits of increased access to mental health services for students and the positive impact on educational outcomes. This contributed to informed discussions and potential policy changes.'),
    ('How do you approach writing a policy brief?', 'When writing a policy brief, I start by clearly defining the issue and its relevance. I conduct comprehensive research to gather evidence and perspectives from various sources. I then analyze the data, identify key findings, and develop actionable recommendations. The brief is structured to present the information concisely and persuasively, ensuring it is accessible to policymakers and stakeholders.'),
    ('What methods do you use to evaluate the impact of a policy?', 'To evaluate the impact of a policy, I use a combination of quantitative and qualitative methods. This includes analyzing statistical data, conducting surveys and interviews, and reviewing relevant case studies. I also consider feedback from stakeholders and experts to assess the effectiveness and potential areas for improvement of the policy.'),
    ('How do you build and maintain relationships with key stakeholders?', 'I build and maintain relationships with key stakeholders by actively engaging with them through regular communication, meetings, and networking events. I prioritize understanding their needs and interests, and I work collaboratively to align our goals. Building trust and demonstrating reliability are crucial in maintaining long-term, positive relationships.'),
    ('Can you describe a successful lobbying campaign you have been part of?', 'As a Summer Law Clerk at Kroger Gardis and Regas LLP, I was involved in a lobbying campaign focused on regulatory relief. I coordinated with stakeholders, led internal meetings, and engaged with legislators to advocate for changes in regulatory policies. The campaign successfully raised awareness and contributed to legislative discussions, showcasing the effectiveness of our strategic efforts.'),
    ('How do you handle opposition from lawmakers or stakeholders?', 'When facing opposition from lawmakers or stakeholders, I approach it with respect and a willingness to listen. I strive to understand their concerns and find common ground. By presenting well-researched arguments and demonstrating the benefits of my position, I aim to persuade them. If compromise is necessary, I work towards solutions that address their concerns while advancing my objectives.'),
    ('What strategies do you use to persuade policymakers?', 'To persuade policymakers, I use a combination of data-driven arguments, personal stories, and stakeholder testimonials. I ensure that my messaging is clear, concise, and aligned with their interests and priorities. Building coalitions and demonstrating broad support for my position also strengthens my persuasive efforts.'),
    ('How do you ensure compliance with lobbying regulations and ethics?', 'Ensuring compliance with lobbying regulations and ethics involves staying informed about the relevant laws and guidelines. I adhere to transparency and disclosure requirements, maintain accurate records of lobbying activities, and prioritize ethical conduct in all interactions. Regular training and consultations with legal experts help me stay updated and compliant with the regulations.')
]

# Add notes (cards) to the deck
for question, answer in questions_answers:
    note = genanki.Note(
        model=my_model,
        fields=[question, answer])
    my_deck.add_note(note)

# Create a package and export it as an .apkg file
my_package = genanki.Package(my_deck)
my_package.write_to_file('interview_questions_deck.apkg')

print("Deck created and saved as 'interview_questions_deck.apkg'")