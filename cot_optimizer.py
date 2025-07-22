
#!/usr/bin/env python3
"""
CLI Chain-of-Thought Prompt Optimizer
Simple command-line tool to enhance prompts with structured reasoning.
"""

import argparse
import sys
import json
from typing import Dict, List, Optional


class CoTOptimizer:
    """Command-line Chain-of-Thought prompt optimizer."""
    
    def __init__(self):
        self.patterns = {
            'math': {
                'name': 'Mathematical Problem Solving',
                'steps': [
                    "1. First, identify what we know and what we need to find",
                    "2. Then, determine which mathematical concepts apply",
                    "3. Next, set up the equations or approach",
                    "4. Finally, solve step by step and verify the answer"
                ],
                'instruction': "Show all your work and reasoning before giving the final answer."
            },
            'coding': {
                'name': 'Code Development',
                'steps': [
                    "1. First, understand the requirements and constraints",
                    "2. Then, plan the algorithm and data structures",
                    "3. Next, consider edge cases and error handling",
                    "4. Finally, implement and test the solution"
                ],
                'instruction': "Show your reasoning for each step before writing the final code."
            },
            'analysis': {
                'name': 'Analytical Thinking',
                'steps': [
                    "1. First, examine the key facts and data",
                    "2. Then, identify patterns and relationships",
                    "3. Next, consider different perspectives",
                    "4. Finally, draw conclusions based on evidence"
                ],
                'instruction': "Think through each step of your analysis before providing conclusions."
            },
            'decision': {
                'name': 'Decision Making',
                'steps': [
                    "1. First, clarify the decision that needs to be made",
                    "2. Then, identify available options and alternatives",
                    "3. Next, evaluate pros and cons of each option",
                    "4. Finally, make a recommendation with clear reasoning"
                ],
                'instruction': "Consider each factor carefully before making your final recommendation."
            },
            'problem': {
                'name': 'Problem Solving',
                'steps': [
                    "1. First, understand what problem we're trying to solve",
                    "2. Then, identify the key components and constraints",
                    "3. Next, consider different approaches",
                    "4. Finally, choose the best solution and explain why"
                ],
                'instruction': "Please walk through each step clearly before giving your final answer."
            },
            'creative': {
                'name': 'Creative Thinking',
                'steps': [
                    "1. First, explore the creative requirements and constraints",
                    "2. Then, brainstorm multiple creative directions",
                    "3. Next, develop the most promising ideas",
                    "4. Finally, refine and present the best creative solution"
                ],
                'instruction': "Show your creative thinking process before presenting your final idea."
            },
            'general': {
                'name': 'General Reasoning',
                'steps': [
                    "1. First, let me understand the question or task",
                    "2. Then, I'll consider what information is relevant",
                    "3. Next, I'll think through different approaches",
                    "4. Finally, I'll provide a clear and complete response"
                ],
                'instruction': "Please reason through each step before giving your final answer."
            }
        }
    
    def detect_type(self, prompt: str) -> str:
        """Detect prompt type using simple keyword matching."""
        prompt_lower = prompt.lower()
        
        # Math keywords
        if any(word in prompt_lower for word in ['calculate', 'solve', 'equation', 'math', 'formula', 'number', 'percent']):
            return 'math'
        
        # Coding keywords
        elif any(word in prompt_lower for word in ['code', 'program', 'function', 'python', 'javascript', 'algorithm', 'debug']):
            return 'coding'
        
        # Analysis keywords
        elif any(word in prompt_lower for word in ['analyze', 'analysis', 'examine', 'evaluate', 'compare', 'study', 'research']):
            return 'analysis'
        
        # Decision keywords
        elif any(word in prompt_lower for word in ['decide', 'choose', 'should', 'recommend', 'option', 'better', 'best']):
            return 'decision'
        
        # Problem solving keywords
        elif any(word in prompt_lower for word in ['problem', 'issue', 'fix', 'solve', 'help', 'trouble']):
            return 'problem'
        
        # Creative keywords
        elif any(word in prompt_lower for word in ['create', 'design', 'write', 'story', 'creative', 'imagine', 'invent']):
            return 'creative'
        
        else:
            return 'general'
    
    def optimize_prompt(self, prompt: str, pattern_type: Optional[str] = None) -> Dict:
        """Optimize a prompt with Chain-of-Thought reasoning."""
        
        # Auto-detect if no type specified
        if pattern_type is None:
            pattern_type = self.detect_type(prompt)
        
        # Get pattern
        if pattern_type not in self.patterns:
            pattern_type = 'general'
        
        pattern = self.patterns[pattern_type]
        
        # Build enhanced prompt
        enhanced_prompt = f"""Original task: {prompt}

Let's approach this step by step:

{chr(10).join(pattern['steps'])}

{pattern['instruction']}"""
        
        # Calculate metrics
        original_words = len(prompt.split())
        enhanced_words = len(enhanced_prompt.split())
        
        return {
            'original_prompt': prompt,
            'enhanced_prompt': enhanced_prompt,
            'pattern_type': pattern_type,
            'pattern_name': pattern['name'],
            'original_words': original_words,
            'enhanced_words': enhanced_words,
            'words_added': enhanced_words - original_words,
            'improvement_ratio': round(enhanced_words / original_words, 2)
        }
    
    def list_patterns(self):
        """List all available patterns."""
        print("Available Chain-of-Thought Patterns:")
        print("=" * 50)
        
        for key, pattern in self.patterns.items():
            print(f"\n{key.upper()} - {pattern['name']}")
            for step in pattern['steps']:
                print(f"  {step}")
    
    def show_examples(self):
        """Show example prompts for each type."""
        examples = {
            'math': "Calculate the compound interest on $5000 at 3% annually for 8 years",
            'coding': "Write a Python function to find the longest palindrome in a string",
            'analysis': "Analyze the pros and cons of remote work for software teams",
            'decision': "Should I invest in stocks or bonds for retirement savings?",
            'problem': "My Python code is running slowly. How can I optimize it?",
            'creative': "Write a short story about an AI that learns to paint"
        }
        
        print("Example Prompts by Type:")
        print("=" * 50)
        
        for prompt_type, example in examples.items():
            print(f"\n{prompt_type.upper()}:")
            print(f"  \"{example}\"")


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description='Chain-of-Thought Prompt Optimizer',
        epilog='Examples:\n'
               '  %(prog)s "Calculate 15%% tip on $45"\n'
               '  %(prog)s "Write a sorting function" --type coding\n'
               '  %(prog)s --examples\n'
               '  %(prog)s --patterns',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('prompt', nargs='?', help='Prompt to optimize')
    parser.add_argument('--type', choices=list(CoTOptimizer().patterns.keys()),
                       help='Specify prompt type (auto-detected if not provided)')
    parser.add_argument('--output', '-o', help='Output file for results')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                       help='Output format (default: text)')
    parser.add_argument('--patterns', action='store_true',
                       help='List all available reasoning patterns')
    parser.add_argument('--examples', action='store_true',
                       help='Show example prompts for each type')
    parser.add_argument('--compare', action='store_true',
                       help='Show before/after comparison')
    
    args = parser.parse_args()
    
    optimizer = CoTOptimizer()
    
    # Handle special commands
    if args.patterns:
        optimizer.list_patterns()
        return 0
    
    if args.examples:
        optimizer.show_examples()
        return 0
    
    if not args.prompt:
        parser.print_help()
        return 1
    
    # Optimize the prompt
    try:
        result = optimizer.optimize_prompt(args.prompt, args.type)
        
        # Generate output
        if args.format == 'json':
            output = json.dumps(result, indent=2)
        else:
            # Text format
            lines = []
            lines.append("CHAIN-OF-THOUGHT PROMPT OPTIMIZER")
            lines.append("=" * 50)
            lines.append(f"Detected Type: {result['pattern_name']} ({result['pattern_type']})")
            lines.append("")
            lines.append("ENHANCED PROMPT:")
            lines.append("-" * 20)
            lines.append(result['enhanced_prompt'])
            
            if args.compare:
                lines.append("")
                lines.append("COMPARISON:")
                lines.append("-" * 20)
                lines.append(f"Original words: {result['original_words']}")
                lines.append(f"Enhanced words: {result['enhanced_words']}")
                lines.append(f"Words added: {result['words_added']}")
                lines.append(f"Improvement ratio: {result['improvement_ratio']}x")
                lines.append("")
                lines.append("ORIGINAL PROMPT:")
                lines.append("-" * 20)
                lines.append(result['original_prompt'])
            
            output = "\n".join(lines)
        
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Results saved to: {args.output}")
        else:
            print(output)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    exit(main())