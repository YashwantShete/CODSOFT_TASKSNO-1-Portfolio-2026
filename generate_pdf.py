import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.graphics.shapes import Drawing, String, Line, Group

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    name_style = ParagraphStyle(
        'NameStyle',
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#000000'),
        textTransform='uppercase'
    )
    
    contact_header_style = ParagraphStyle(
        'ContactHeaderStyle',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#333333'),
        textTransform='uppercase'
    )
    
    contact_detail_style = ParagraphStyle(
        'ContactDetailStyle',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor('#222222')
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitleStyle',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#222222'),
        textTransform='uppercase',
        spaceAfter=6
    )
    
    summary_text_style = ParagraphStyle(
        'SummaryTextStyle',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor('#333333')
    )
    
    skill_style = ParagraphStyle(
        'SkillStyle',
        fontName='Helvetica',
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor('#111111')
    )
    
    edu_year_style = ParagraphStyle(
        'EduYearStyle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#000000')
    )
    
    edu_title_style = ParagraphStyle(
        'EduTitleStyle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#111111')
    )
    
    edu_inst_style = ParagraphStyle(
        'EduInstStyle',
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#444444')
    )
    
    cert_style = ParagraphStyle(
        'CertStyle',
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#333333')
    )
    
    hobby_style = ParagraphStyle(
        'HobbyStyle',
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor('#222222')
    )

    story = []
    
    # ------------------ HEADER SECTION ------------------
    header_left = Paragraph("YASHWANT<br/>RAVINDRA<br/>SHETE", name_style)
    header_right = [
        Paragraph("CONTACT", contact_header_style),
        Spacer(1, 6),
        Paragraph("<b>&#9742;</b> 8530511202", contact_detail_style),
        Paragraph("<b>&#9993;</b> yashwantshete2424@gmail.com", contact_detail_style)
    ]
    
    header_table = Table([[header_left, header_right]], colWidths=[320, 195])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 24))
    
    # ------------------ SUMMARY SECTION ------------------
    story.append(Paragraph("SUMMARY", section_title_style))
    story.append(Spacer(1, 4))
    summary_p = Paragraph(
        "I'm a BCA student, currently in my third year, looking for an internship to gain real-world experience. "
        "I'm eager to learn, grow my skills, and contribute wherever I can.",
        summary_text_style
    )
    story.append(summary_p)
    story.append(Spacer(1, 22))
    
    # ------------------ THE FOUNDATION SECTION ------------------
    story.append(Paragraph("THE FOUNDATION", section_title_style))
    story.append(Spacer(1, 6))
    
    left_skills = [
        Paragraph("Python", skill_style),
        Paragraph("Java", skill_style),
        Paragraph("MongoDB", skill_style),
        Paragraph("DBMS", skill_style),
        Paragraph("C Programming", skill_style),
    ]
    
    right_skills = [
        Paragraph("HTML", skill_style),
        Paragraph("CSS", skill_style),
        Paragraph("AI Prompting", skill_style),
        Paragraph("MS Office", skill_style),
        Paragraph("Problem Solving", skill_style),
    ]
    
    skills_data = []
    for l, r in zip(left_skills, right_skills):
        skills_data.append([l, r])
        
    skills_table = Table(skills_data, colWidths=[240, 275])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 24))
    
    # ------------------ EDUCATION & CERTIFICATIONS / HOBBIES ------------------
    # Left Column: Education
    edu_content = [
        Paragraph("EDUCATION", section_title_style),
        Spacer(1, 6),
        Paragraph("2026", edu_year_style),
        Paragraph("BCA (Third Year) | Ongoing", edu_title_style),
        Paragraph("[University Affiliated College, Ahilyanagar]", edu_inst_style),
        Spacer(1, 10),
        Paragraph("2023 - 2024", edu_year_style),
        Paragraph("12th (HSC) | 67.33%", edu_title_style),
        Paragraph("Pemraj Sarda College, Ahilyanagar", edu_inst_style),
        Spacer(1, 10),
        Paragraph("2021 - 2022", edu_year_style),
        Paragraph("10th (SSC) | 70.80%", edu_title_style),
        Paragraph("Sacred Heart Convent High School, Ahilyanagar.", edu_inst_style),
    ]
    
    # Right Column: Certifications + Hobbies
    cert_p = Paragraph(
        "<b>March 2026:</b> Certificate in \"Flui English Speaking and Mastering Communication Skills,\" "
        "One-Day Workshop, Department of English, New Arts, Commerce, and Science College, Ahilyanagar.",
        cert_style
    )
    
    hobbies_content = [
        cert_p,
        Spacer(1, 20),
        Paragraph("HOBBIES", section_title_style),
        Spacer(1, 6),
        Paragraph("&bull; Travelling", hobby_style),
        Paragraph("&bull; Football", hobby_style),
        Paragraph("&bull; Reading", hobby_style),
    ]
    
    split_table = Table([[edu_content, hobbies_content]], colWidths=[260, 255])
    split_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(split_table)
    
    doc.build(story)

if __name__ == '__main__':
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    output_pdf_1 = os.path.join(workspace_dir, "resume.pdf")
    output_pdf_2 = os.path.join(workspace_dir, "Yashwant_Shete_Resume.pdf")
    output_pdf_3 = os.path.join(workspace_dir, "portfolio_app", "static", "resume.pdf")
    
    build_pdf(output_pdf_1)
    build_pdf(output_pdf_2)
    build_pdf(output_pdf_3)
    print("PDF generation complete!")
