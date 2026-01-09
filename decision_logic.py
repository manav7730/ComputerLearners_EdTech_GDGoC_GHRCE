def compare_paths(goal, level, style):
    paths = {
        "Video-based learning": {
            "pros": ["Easy to understand", "Visual explanation", "Beginner friendly"],
            "cons": ["Passive learning", "Less practice"]
        },
        "Text-based learning": {
            "pros": ["Detailed explanation", "Good for revision", "Self-paced"],
            "cons": ["Can feel boring", "Hard for beginners"]
        },
        "Practice-first learning": {
            "pros": ["Hands-on experience", "Fast skill building", "Good retention"],
            "cons": ["Can be confusing initially", "Needs guidance"]
        }
    }

    insight = (
        "If you are a beginner, start with video-based learning.\n"
        "If you prefer deep understanding, choose text-based resources.\n"
        "If your goal is skill mastery, practice-first works best."
    )

    return paths, insight