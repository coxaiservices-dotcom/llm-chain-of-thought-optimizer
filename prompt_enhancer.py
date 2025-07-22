#!/usr/bin/env python3
"""
Prompt Enhancement Tool
Improves prompts by adding specificity, context, constraints, and better instructions.
"""

import argparse
import sys


def enhance_prompt(prompt, prompt_type=None):
    """Enhance a prompt by making it more specific and effective."""
    
    # Auto-detect type if not specified
    if prompt_type is None:
        prompt_type = detect_type(prompt)
    
    # Get enhancement rules for the detected type
    enhancer = get_enhancer(prompt_type)
    
    # Apply enhancements
    enhanced = enhancer(prompt)
    
    return {
        'original_prompt': prompt,
        'enhanced_prompt': enhanced,
        'prompt_type': prompt_type,
        'improvements': get_improvements(prompt, enhanced, prompt_type)
    }


def detect_type(prompt):
    """Detect what type of prompt this is."""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ['calculate', 'solve', 'math', 'equation', 'percent', 'number']):
        return 'math'
    elif any(word in prompt_lower for word in ['function', 'code', 'program', 'algorithm', 'write', 'implement']):
        return 'coding'
    elif any(word in prompt_lower for word in ['analyze', 'analysis', 'examine', 'evaluate', 'compare', 'study']):
        return 'analysis'
    elif any(word in prompt_lower for word in ['explain', 'describe', 'what is', 'how does', 'tell me']):
        return 'explanation'
    elif any(word in prompt_lower for word in ['should', 'recommend', 'choose', 'decide', 'better', 'best']):
        return 'decision'
    elif any(word in prompt_lower for word in ['create', 'design', 'write', 'story', 'poem', 'creative']):
        return 'creative'
    elif any(word in prompt_lower for word in ['problem', 'issue', 'fix', 'troubleshoot', 'debug']):
        return 'problem'
    else:
        return 'general'


def get_enhancer(prompt_type):
    """Get the enhancement function for a specific prompt type."""
    enhancers = {
        'math': enhance_math_prompt,
        'coding': enhance_coding_prompt,
        'analysis': enhance_analysis_prompt,
        'explanation': enhance_explanation_prompt,
        'decision': enhance_decision_prompt,
        'creative': enhance_creative_prompt,
        'problem': enhance_problem_prompt,
        'general': enhance_general_prompt
    }
    
    return enhancers.get(prompt_type, enhance_general_prompt)


def enhance_math_prompt(prompt):
    """Enhance math-related prompts."""
    enhanced = prompt
    
    # Add specificity if missing
    if 'show' not in prompt.lower():
        enhanced += ". Show all steps in your calculation."
    
    # Add verification request
    if 'verify' not in prompt.lower() and 'check' not in prompt.lower():
        enhanced += " Verify your answer and explain your reasoning."
    
    # Add format request if dealing with money/percentages
    if any(symbol in prompt for symbol in ['$', '%', 'percent', 'dollar']):
        enhanced += " Format monetary amounts clearly and round appropriately."
    
    # Add context for word problems
    if len(prompt.split()) > 8:  # Likely a word problem
        enhanced = "Solve this step-by-step: " + enhanced
    
    return enhanced


def enhance_coding_prompt(prompt):
    """Enhance coding-related prompts."""
    base = prompt
    
    # Add language specification if missing
    if not any(lang in prompt.lower() for lang in ['python', 'javascript', 'java', 'c++', 'c#']):
        base = f"Write a Python {base.lower()}"
    
    enhancements = []
    
    # Add specific requirements
    if 'function' in prompt.lower():
        enhancements.extend([
            "Include proper type hints",
            "Add a comprehensive docstring with examples",
            "Handle edge cases appropriately",
            "Consider time and space complexity"
        ])
    
    # Add code quality requirements
    enhancements.extend([
        "Follow best practices and clean code principles",
        "Include error handling where appropriate",
        "Add comments for complex logic"
    ])
    
    # Combine base prompt with enhancements
    enhanced = f"{base}. Requirements: {', '.join(enhancements)}."
    
    return enhanced


def enhance_analysis_prompt(prompt):
    """Enhance analysis-related prompts."""
    enhanced = prompt
    
    # Add structure request
    if 'structure' not in prompt.lower():
        enhanced += " Structure your analysis with clear sections: overview, key findings, and conclusions."
    
    # Add evidence requirement
    if 'evidence' not in prompt.lower() and 'data' not in prompt.lower():
        enhanced += " Support your analysis with specific evidence and examples."
    
    # Add perspective requirement
    enhanced += " Consider multiple perspectives and potential counterarguments."
    
    # Add actionable insights request
    enhanced += " Provide actionable insights and recommendations based on your analysis."
    
    return enhanced


def enhance_explanation_prompt(prompt):
    """Enhance explanation-related prompts."""
    enhanced = prompt
    
    # Add audience specification
    if 'explain' in prompt.lower() and 'like' not in prompt.lower():
        enhanced += " Explain in simple terms that a general audience can understand."
    
    # Add structure request
    enhanced += " Use clear examples and analogies to illustrate your points."
    
    # Add comprehensive coverage
    enhanced += " Cover the key concepts, how it works, and why it matters."
    
    return enhanced


def enhance_decision_prompt(prompt):
    """Enhance decision-related prompts."""
    enhanced = prompt
    
    # Add criteria request
    enhanced += " Consider the key factors: cost, benefits, risks, and long-term implications."
    
    # Add structure
    enhanced += " Provide a clear recommendation with pros and cons for each option."
    
    # Add personalization
    enhanced += " Tailor your advice to different situations or preferences."
    
    return enhanced


def enhance_creative_prompt(prompt):
    """Enhance creative prompts."""
    enhanced = prompt
    
    # Add specificity for creative tasks
    if 'story' in prompt.lower():
        enhanced += " Include compelling characters, clear plot structure, and vivid descriptions."
    elif 'design' in prompt.lower():
        enhanced += " Consider user experience, aesthetics, and functionality."
    
    # Add creativity boosters
    enhanced += " Be creative and original in your approach."
    
    return enhanced


def enhance_problem_prompt(prompt):
    """Enhance problem-solving prompts."""
    enhanced = "Help me troubleshoot this issue: " + prompt
    
    # Add systematic approach
    enhanced += " Provide a systematic approach to identify and solve the problem."
    
    # Add prevention
    enhanced += " Include steps to prevent this issue in the future."
    
    return enhanced


def enhance_general_prompt(prompt):
    """Enhance general prompts."""
    enhanced = prompt
    
    # Add clarity request
    enhanced += " Provide a clear, comprehensive response with specific details."
    
    # Add structure
    enhanced += " Organize your response logically with examples where helpful."
    
    return enhanced


def get_improvements(original, enhanced, prompt_type):
    """List what improvements were made."""
    improvements = []
    
    if len(enhanced) > len(original):
        improvements.append(f"Expanded from {len(original.split())} to {len(enhanced.split())} words")
    
    # Type-specific improvements
    if prompt_type == 'coding':
        improvements.extend([
            "Added language specification",
            "Included code quality requirements",
            "Added documentation requirements",
            "Specified error handling needs"
        ])
    elif prompt_type == 'math':
        improvements.extend([
            "Added step-by-step requirement",
            "Included verification request",
            "Added formatting guidelines"
        ])
    elif prompt_type == 'analysis':
        improvements.extend([
            "Added structural requirements",
            "Included evidence requirements",
            "Added multiple perspective consideration"
        ])
    else:
        improvements.extend([
            "Added clarity requirements",
            "Included specificity improvements",
            "Added structural guidance"
        ])
    
    return improvements


def show_examples():
    """Show before/after examples."""
    examples = [
        ("Math", "Calculate 15% tip", "Calculate 15% tip on the bill. Show all steps in your calculation. Verify your answer and explain your reasoning. Format monetary amounts clearly and round appropriately."),
        ("Coding", "Write a sorting function", "Write a Python sorting function. Requirements: Include proper type hints, Add a comprehensive docstring with examples, Handle edge cases appropriately, Consider time and space complexity, Follow best practices and clean code principles, Include error handling where appropriate, Add comments for complex logic."),
        ("Analysis", "Analyze remote work", "Analyze remote work. Structure your analysis with clear sections: overview, key findings, and conclusions. Support your analysis with specific evidence and examples. Consider multiple perspectives and potential counterarguments. Provide actionable insights and recommendations based on your analysis."),
    ]
    
    print("BEFORE/AFTER EXAMPLES:")
    print("=" * 60)
    
    for category, before, after in examples:
        print(f"\n{category.upper()}:")
        print(f"Before: {before}")
        print(f"After:  {after}")


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description='Prompt Enhancement Tool - Actually improves your prompts')
    parser.add_argument('prompt', nargs='?', help='Prompt to enhance')
    parser.add_argument('--type', choices=['math', 'coding', 'analysis', 'explanation', 'decision', 'creative', 'problem', 'general'],
                       help='Specify prompt type')
    parser.add_argument('--examples', action='store_true', help='Show before/after examples')
    parser.add_argument('--compare', action='store_true', help='Show detailed comparison')
    
    args = parser.parse_args()
    
    # Show examples
    if args.examples:
        show_examples()
        return
    
    # Check for prompt
    if not args.prompt:
        print("Error: Please provide a prompt to enhance")
        print("Usage: python prompt_enhancer.py \"Your prompt here\"")
        print("       python prompt_enhancer.py --examples")
        return
    
    # Enhance the prompt
    try:
        result = enhance_prompt(args.prompt, args.type)
        
        print("PROMPT ENHANCEMENT TOOL")
        print("=" * 50)
        print(f"Detected Type: {result['prompt_type'].title()}")
        print()
        print("ENHANCED PROMPT:")
        print("-" * 20)
        print(result['enhanced_prompt'])
        
        if args.compare:
            print()
            print("COMPARISON:")
            print("-" * 20)
            print(f"Original: {result['original_prompt']}")
            print()
            print("IMPROVEMENTS MADE:")
            for improvement in result['improvements']:
                print(f"• {improvement}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()