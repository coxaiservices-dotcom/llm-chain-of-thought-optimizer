# 🧠 CLI Chain-of-Thought Optimizer

A simple command-line tool that enhances prompts with structured reasoning patterns to improve AI response quality.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![No Dependencies](https://img.shields.io/badge/dependencies-none-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/coxaiservices/cli-chain-of-thought-optimizer.git
cd cli-chain-of-thought-optimizer

# No dependencies to install - uses only Python standard library!
# Just run it:
python cot_optimizer.py --examples
```

### Basic Usage
```bash
# Enhance any prompt
python cot_optimizer.py "Calculate 15% tip on a $45 bill"

# Specify prompt type
python cot_optimizer.py "Write a sorting function" --type coding

# Show before/after comparison
python cot_optimizer.py "Analyze iPhone vs Android" --compare

# Save results to file
python cot_optimizer.py "Should I invest in stocks?" --output result.txt

# JSON output format
python cot_optimizer.py "Debug my code" --format json
```

## ✨ Features

- 🎯 **Auto-detects prompt type** (math, coding, analysis, decision, problem, creative)
- 📝 **6 reasoning patterns** optimized for different tasks
- 💾 **Multiple output formats** (text, JSON)
- 📊 **Before/after comparison** with metrics
- 🔧 **Zero dependencies** - uses only Python standard library
- 📚 **Built-in examples** and pattern reference

## 🛠️ Command Options

```bash
python cot_optimizer.py [PROMPT] [OPTIONS]

Arguments:
  PROMPT                    Prompt to optimize

Options:
  --type {math,coding,analysis,decision,problem,creative,general}
                           Specify prompt type (auto-detected if not provided)
  --output, -o FILE        Output file for results
  --format {text,json}     Output format (default: text)
  --compare                Show before/after comparison
  --patterns               List all available reasoning patterns
  --examples               Show example prompts for each type
  --help, -h               Show help message
```

## 📚 Examples

### Math Problem
```bash
$ python cot_optimizer.py "Calculate compound interest on $5000 at 3% for 8 years"

ENHANCED PROMPT:
Original task: Calculate compound interest on $5000 at 3% for 8 years

Let's approach this step by step:
1. First, identify what we know and what we need to find
2. Then, determine which mathematical concepts apply
3. Next, set up the equations or approach
4. Finally, solve step by step and verify the answer

Show all your work and reasoning before giving the final answer.
```

### Coding Task
```bash
$ python cot_optimizer.py "Write a function to reverse a string" --type coding

ENHANCED PROMPT:
Original task: Write a function to reverse a string

Let's approach this step by step:
1. First, understand the requirements and constraints
2. Then, plan the algorithm and data structures
3. Next, consider edge cases and error handling
4. Finally, implement and test the solution

Show your reasoning for each step before writing the final code.
```

## 🎯 Reasoning Patterns

The tool includes 6 specialized reasoning patterns:

- **Math**: Mathematical problem solving with verification
- **Coding**: Algorithm planning and implementation
- **Analysis**: Systematic examination and conclusion drawing
- **Decision**: Option evaluation and recommendation
- **Problem**: Issue identification and solution finding
- **Creative**: Ideation and creative development
- **General**: Universal reasoning framework

## 📊 Output Formats

### Text Format (Default)
Human-readable output with clear sections and formatting.

### JSON Format
Structured data for programmatic use:
```json
{
  "original_prompt": "Calculate 15% tip",
  "enhanced_prompt": "Original task: ...",
  "pattern_type": "math",
  "pattern_name": "Mathematical Problem Solving",
  "original_words": 4,
  "enhanced_words": 45,
  "words_added": 41,
  "improvement_ratio": 11.25
}
```

## 🔧 Development

### Requirements
- Python 3.6+ (no external dependencies)
- Standard library modules: `argparse`, `json`, `sys`, `typing`

### Testing
```bash
# Test all pattern types
python cot_optimizer.py --examples

# Test specific functionality
python cot_optimizer.py "test prompt" --compare --format json
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mark Cox** - AI Software Engineer & Prompt Engineering Specialist
- LinkedIn: [coxaiservices](https://linkedin.com/in/coxaiservices)
- GitHub: [@coxaiservices](https://github.com/coxaiservices)

## 🙏 Acknowledgments

- Inspired by chain-of-thought reasoning research
- Built for practical prompt engineering applications
- Designed for simplicity and reliability