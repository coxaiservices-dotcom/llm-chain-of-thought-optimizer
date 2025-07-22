#!/usr/bin/env python3
"""
Free AI Prompt Improver
Uses free Hugging Face models (no API key required) to improve prompts.
"""

import argparse
import sys


def improve_prompt_with_free_ai(prompt):
    """Use free Hugging Face models to improve prompts."""
    
    # Try to use Hugging Face transformers
    try:
        from transformers import pipeline, set_seed
        
        print("🤖 Loading free AI model (this may take a moment)...")
        
        # Use a free text generation model
        # We'll use a smaller model that works without API keys
        generator = pipeline(
            'text-generation',
            model='microsoft/DialoGPT-medium',
            tokenizer='microsoft/DialoGPT-medium',
            device=-1  # Use CPU (works on all machines)
        )
        
        # Create improvement prompt
        improvement_request = f"""Improve this prompt to make it more effective:

Original: "{prompt}"

Better version:"""
        
        # Generate improved prompt
        set_seed(42)  # For consistent results
        result = generator(
            improvement_request,
            max_length=200,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
            pad_token_id=generator.tokenizer.eos_token_id
        )
        
        # Extract the improved prompt
        generated_text = result[0]['generated_text']
        improved_prompt = generated_text.split("Better version:")[-1].strip()
        
        # Clean up the result
        if improved_prompt:
            return {
                'original_prompt': prompt,
                'improved_prompt': improved_prompt,
                'method': 'Free AI (Hugging Face)',
                'success': True
            }
        else:
            raise Exception("No improvement generated")
            
    except ImportError:
        print("⚠️ Transformers not installed. Using rule-based improvement.")
        return improve_prompt_manually(prompt)
    except Exception as e:
        print(f"⚠️ AI model error: {e}. Using rule-based improvement.")
        return improve_prompt_manually(prompt)


def improve_prompt_manually(prompt):
    """Fallback: Improve prompt using smart rules."""
    
    # Detect prompt type
    prompt_type = detect_prompt_type(prompt)
    
    # Apply type-specific improvements
    improvements = {
        'coding': improve_coding_prompt,
        'math': improve_math_prompt,
        'analysis': improve_analysis_prompt,
        'creative': improve_creative_prompt,
        'explanation': improve_explanation_prompt,
        'decision': improve_decision_prompt
    }
    
    improver = improvements.get(prompt_type, improve_general_prompt)
    improved = improver(prompt)
    
    return {
        'original_prompt': prompt,
        'improved_prompt': improved,
        'method': 'Smart Rules',
        'success': True
    }


def detect_prompt_type(prompt):
    """Detect what type of prompt this is."""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ['function', 'code', 'program', 'algorithm', 'write', 'implement']):
        return 'coding'
    elif any(word in prompt_lower for word in ['calculate', 'solve', 'math', 'equation', 'formula']):
        return 'math'
    elif any(word in prompt_lower for word in ['analyze', 'compare', 'evaluate', 'study', 'examine']):
        return 'analysis'
    elif any(word in prompt_lower for word in ['create', 'design', 'story', 'poem', 'creative', 'write']):
        return 'creative'
    elif any(word in prompt_lower for word in ['explain', 'describe', 'what is', 'how does', 'tell me']):
        return 'explanation'
    elif any(word in prompt_lower for word in ['should', 'recommend', 'choose', 'decide', 'better']):
        return 'decision'
    else:
        return 'general'


def improve_coding_prompt(prompt):
    """Improve coding prompts with specific requirements."""
    if 'python' not in prompt.lower():
        base = f"Write a Python {prompt.lower()}"
    else:
        base = prompt
    
    return f"""{base}

Requirements:
• Include proper type hints and docstring with examples
• Handle edge cases and potential errors
• Follow PEP 8 style guidelines and best practices
• Add clear comments explaining the logic
• Include example usage and test cases
• Consider time and space complexity

Provide clean, production-ready code."""


def improve_math_prompt(prompt):
    """Improve math prompts with step-by-step requirements."""
    return f"""{prompt}

Please:
• Show all calculation steps clearly
• Explain the reasoning behind each step
• Use proper mathematical notation
• Verify the final answer
• Include units where applicable
• Provide a real-world context if helpful"""


def improve_analysis_prompt(prompt):
    """Improve analysis prompts with structure."""
    return f"""{prompt}

Structure your analysis with:
• Clear introduction and context
• Key findings with supporting evidence
• Multiple perspectives where relevant
• Specific examples and data points
• Actionable insights and recommendations
• Well-organized conclusion

Use clear headings and logical flow."""


def improve_creative_prompt(prompt):
    """Improve creative prompts."""
    return f"""{prompt}

Creative requirements:
• Be original and engaging
• Include vivid descriptions and details
• Develop a clear structure (beginning, middle, end)
• Create compelling characters or concepts
• Use appropriate tone and style
• Show creativity while staying on topic"""


def improve_explanation_prompt(prompt):
    """Improve explanation prompts."""
    return f"""{prompt}

Please provide:
• A clear, easy-to-understand explanation
• Real-world examples and analogies
• Step-by-step breakdown of key concepts
• Context for why this topic matters
• Common misconceptions addressed
• Summary of main takeaways

Tailor the explanation for a general audience."""


def improve_decision_prompt(prompt):
    """Improve decision-making prompts."""
    return f"""{prompt}

Please consider:
• All available options and alternatives
• Pros and cons of each choice
• Key factors: cost, benefits, risks, timeline
• Short-term and long-term implications
• Different scenarios or use cases
• Clear recommendation with reasoning

Provide a structured decision framework."""


def improve_general_prompt(prompt):
    """Improve general prompts."""
    return f"""{prompt}

Please provide:
• A comprehensive and well-structured response
• Specific details and concrete examples
• Clear reasoning for any claims or recommendations
• Practical, actionable information
• Proper organization with logical flow
• Summary of key points"""


def show_examples():
    """Show before/after improvement examples."""
    examples = [
        {
            'type': 'Coding',
            'original': 'Write a sorting function',
            'improved': '''Write a Python sorting function

Requirements:
• Include proper type hints and docstring with examples
• Handle edge cases and potential errors
• Follow PEP 8 style guidelines and best practices
• Add clear comments explaining the logic
• Include example usage and test cases
• Consider time and space complexity

Provide clean, production-ready code.'''
        },
        {
            'type': 'Math',
            'original': 'Calculate 15% tip',
            'improved': '''Calculate 15% tip

Please:
• Show all calculation steps clearly
• Explain the reasoning behind each step
• Use proper mathematical notation
• Verify the final answer
• Include units where applicable
• Provide a real-world context if helpful'''
        },
        {
            'type': 'Analysis',
            'original': 'Compare iPhone vs Android',
            'improved': '''Compare iPhone vs Android

Structure your analysis with:
• Clear introduction and context
• Key findings with supporting evidence
• Multiple perspectives where relevant
• Specific examples and data points
• Actionable insights and recommendations
• Well-organized conclusion

Use clear headings and logical flow.'''
        }
    ]
    
    print("BEFORE/AFTER EXAMPLES:")
    print("=" * 60)
    
    for example in examples:
        print(f"\n{example['type'].upper()}:")
        print(f"Before: {example['original']}")
        print(f"After:  {example['improved']}")
        print("-" * 60)


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description='Free AI Prompt Improver (No API Key Required)')
    parser.add_argument('prompt', nargs='?', help='Prompt to improve')
    parser.add_argument('--examples', action='store_true', help='Show before/after examples')
    parser.add_argument('--compare', action='store_true', help='Show detailed comparison')
    parser.add_argument('--manual', action='store_true', help='Skip AI and use rules only')
    
    args = parser.parse_args()
    
    # Show examples
    if args.examples:
        show_examples()
        return
    
    # Check for prompt
    if not args.prompt:
        print("FREE AI PROMPT IMPROVER")
        print("=" * 40)
        print("No API key required! Uses free AI models.")
        print()
        print("Usage: python free_ai_improver.py \"Your prompt here\"")
        print("       python free_ai_improver.py --examples")
        print()
        print("📦 Install transformers for AI mode: pip install transformers torch")
        return
    
    # Improve the prompt
    try:
        if args.manual:
            result = improve_prompt_manually(args.prompt)
        else:
            result = improve_prompt_with_free_ai(args.prompt)
        
        print("FREE AI PROMPT IMPROVER")
        print("=" * 50)
        print(f"Method: {result['method']}")
        print()
        print("IMPROVED PROMPT:")
        print("-" * 20)
        print(result['improved_prompt'])
        
        if args.compare:
            print()
            print("ORIGINAL PROMPT:")
            print("-" * 20)
            print(result['original_prompt'])
            print()
            print("IMPROVEMENTS:")
            print("-" * 20)
            original_words = len(result['original_prompt'].split())
            improved_words = len(result['improved_prompt'].split())
            print(f"• Expanded from {original_words} to {improved_words} words")
            print(f"• Added specific requirements and structure")
            print(f"• Improved clarity and completeness")
            print(f"• Enhanced with best practices")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()