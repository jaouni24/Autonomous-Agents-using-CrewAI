from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context) -> Task:
        """
        Task to research the about meeting participants and companies before the meeting.
        """
        return Task(
            name="Research Agent",
            description=dedent("""
                Conduct comprehensive research on each of the individuals and companies involved 
                in the upcoming meeting. Gather information on recent news, achievements, professional 
                background and any relevant business activities.
                
                participants: {meeting_participants}
                context: {meeting_context}"""),

            expected_output=dedent(""" 
                A detailed report summarizing the findings on each participant, 
                highlighting key points that could be useful for the meeting. """),
            
            agent=agent,

            async_execution=True
        )

    def industry_analysis_task(self, agent, meeting_participants, meeting_context) -> Task:
        """
        Task to analyze the current trends and challenges in a specific industry.
        """
        return Task(
            name="Industry Analysis Agent",
            description=dedent("""
			    Analyze the current industry trends, challenges, and opportunities
				relevant to the meeting's context. Consider market reports, recent
				developments, and expert opinions to provide a comprehensive
				overview of the industry landscape.
                               
                participants: {meeting_participants}
                context: {meeting_context}"""),

            expected_output=dedent(""" 
                An insightful analysis that identifies major trends, potential
				challenges, and strategic opportunities."""),

			async_execution=True,

			agent=agent
        )
    
    def meeting_strategy_task(self, agent, meeting_context, meeting_objective):
        return Task(
            name="Meeting Strategy Agent",
            description=dedent(f"""\
                Develop strategic talking points, questions, and discussion angles
                for the meeting based on the research and industry analysis conducted

                Meeting Context: {meeting_context}
                Meeting Objective: {meeting_objective}"""),
            expected_output=dedent("""\
                Complete report with a list of key talking points, strategic questions
                to ask to help achieve the meetings objective during the meeting."""),
            agent=agent
    )
    
    def summary_and_briefing_task(self, agent, meeting_context, meeting_objective):
        return Task(
            name="Summary and Briefing Agent",
            description=dedent(f"""\
                Compile all the research findings, industry analysis, and strategic
                talking points into a concise, comprehensive briefing document for
                the meeting.
                Ensure the briefing is easy to digest and equips the meeting
                participants with all necessary information and strategies.

                Meeting Context: {meeting_context}
                Meeting Objective: {meeting_objective}"""),
            expected_output=dedent("""\
                A well-structured briefing document that includes sections for
                participant bios, industry overview, talking points, and
                strategic recommendations."""),
            agent=agent
        )