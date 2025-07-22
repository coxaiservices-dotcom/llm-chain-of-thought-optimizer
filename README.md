# 🤖 Free AI Prompt Improver

A powerful command-line tool that enhances prompts for better AI responses using **free models** - no API keys required!

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![No API Keys](https://img.shields.io/badge/API%20keys-not%20required-green.svg)
![Free Models](https://img.shields.io/badge/models-free%20%26%20local-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- 🆓 **Completely Free** - No API keys, no costs, no limits
- 🤖 **AI-Powered** - Uses Hugging Face transformers (optional)
- 🔧 **Smart Fallback** - Works even without AI models installed
- 📊 **Multiple Modes** - AI enhancement or rule-based improvements
- 🎯 **Type-Aware** - Optimizes for coding, math, analysis, creative tasks
- ⚡ **Fast & Reliable** - Works offline once models are downloaded

## 🚀 Quick Start

### Basic Installation (No Dependencies)
```bash
# Clone or download
git clone https://github.com/coxaiservices/free-ai-prompt-improver.git
cd free-ai-prompt-improver

# Works immediately with zero dependencies!
python3 free_ai_improver.py "Write a sorting function"
```

### Enhanced Installation (With AI Models)
```bash
# Install AI dependencies for enhanced mode
pip install transformers torch

# Now you get AI-powered improvements
python3 free_ai_improver.py "Write a sorting function"
```

## 💡 Usage Examples

### Basic Usage
```bash
# Improve any prompt
python3 free_ai_improver.py "Calculate compound interest"

# Show before/after comparison
python3 free_ai_improver.py "Analyze climate data" --compare

# Force rule-based mode (skip AI)
python3 free_ai_improver.py "Create a web app" --manual

# See example improvements
python3 free_ai_improver.py --examples
```

### Real Examples

**Before:**
```
"Write a sorting function"
```

**After:**
```
Write a Python sorting function

Requirements:
• Include proper type hints and docstring with examples
• Handle edge cases and potential errors
• Follow PEP 8 style guidelines and best practices
• Add clear comments explaining the logic
• Include example usage and test cases
• Consider time and space complexity

Provide clean, production-ready code.
```

## 🛠️ How It Works

### Two Enhancement Modes

**1. AI Mode (Enhanced)**
- Uses free Hugging Face transformer models
- Downloads models locally (one-time setup)
- Provides intelligent, context-aware improvements
- Works completely offline after initial download

**2. Smart Rules Mode (Fallback)**
- Uses advanced rule-based improvements
- Zero dependencies required
- Instant results
- Type-aware enhancements

### Automatic Fallback
If AI models aren't available, the tool automatically switches to smart rules mode - you always get improved prompts!

## 📊 Supported Prompt Types

| Type | Examples | Improvements Added |
|------|----------|-------------------|
| **Coding** | "Write a function", "Debug this code" | Type hints, error handling, best practices |
| **Math** | "Calculate interest", "Solve equation" | Step-by-step requirements, verification |
| **Analysis** | "Compare options", "Analyze data" | Structure, evidence, multiple perspectives |
| **Creative** | "Write a story", "Design logo" | Originality, structure, engagement |
| **Explanation** | "Explain AI", "How does X work" | Clarity, examples, audience consideration |
| **Decision** | "Should I buy?", "Choose between" | Criteria, pros/cons, recommendations |

## 🔧 Command Options

```bash
python3 free_ai_improver.py [PROMPT] [OPTIONS]

Arguments:
  PROMPT                    Prompt to improve

Options:
  --compare                 Show before/after comparison with metrics
  --examples                Display example improvements for different types
  --manual                  Skip AI mode and use smart rules only
  --help, -h               Show help message
```

## 📦 Installation Options

### Option 1: Minimal (Rule-based only)
```bash
# No installation needed - just Python!
python3 free_ai_improver.py "Your prompt here"
```

### Option 2: Full AI Features
```bash
# Install transformer dependencies
pip install -r requirements.txt

# First run downloads models (one-time, ~500MB)
python3 free_ai_improver.py "Your prompt here"
```

### Option 3: Docker (Coming Soon)
```bash
docker run -it free-ai-improver "Your prompt here"
```

## 🎯 Use Cases

### For Developers
- Improve coding prompts for better AI-generated code
- Add best practices and requirements automatically
- Enhance technical documentation requests

### For Students
- Better homework and research prompts
- Improved explanations and learning requests
- Enhanced creative writing prompts

### For Professionals
- Business analysis and decision-making prompts
- Technical writing and documentation
- Training and educational content

### For AI Practitioners
- Prompt engineering experimentation
- A/B testing different prompt versions
- Learning prompt optimization techniques

## 🔍 Technical Details

### AI Models Used
- **Text Generation**: Microsoft DialoGPT-medium (free)
- **Runs Locally**: No data sent to external servers
- **CPU Compatible**: Works without GPU
- **Offline Capable**: After initial model download

### Performance
- **Rule Mode**: Instant results
- **AI Mode**: 2-5 seconds (after models loaded)
- **Memory Usage**: ~500MB when AI models loaded
- **Storage**: ~500MB for downloaded models

## 📈 Comparison

| Feature | This Tool | ChatGPT API | Other Tools |
|---------|-----------|-------------|-------------|
| **Cost** | Free | $0.002/1K tokens | Varies |
| **API Key** | None | Required | Usually required |
| **Offline** | Yes | No | Usually no |
| **Privacy** | Local only | Data sent to OpenAI | Varies |
| **Limits** | None | Token/rate limits | Varies |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Clone for development
git clone https://github.com/coxaiservices/free-ai-prompt-improver.git
cd free-ai-prompt-improver

# Install development dependencies
pip install -r requirements.txt

# Run tests
python3 -m pytest tests/

# Test different modes
python3 free_ai_improver.py --examples
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mark Cox** - AI Software Engineer & Prompt Engineering Specialist

- 🔗 LinkedIn: [coxaiservices](https://linkedin.com/in/coxaiservices)
- 🐙 GitHub: [@coxaiservices](https://github.com/coxaiservices)
- 📧 Email: coxaiservices@gmail.com

*Built with expertise in prompt engineering, AI model integration, and practical software development.*

## 🙏 Acknowledgments

- **Hugging Face** for providing free, high-quality transformer models
- **Microsoft** for the DialoGPT model
- **Open source community** for making AI accessible to everyone

## 🔮 Roadmap

- [ ] Support for more AI models (Llama, Claude, etc.)
- [ ] Web interface version
- [ ] Batch processing for multiple prompts
- [ ] Custom improvement templates
- [ ] Integration with popular AI tools
- [ ] Performance benchmarking suite

---

⭐ **Star this repo if it helps with your prompt engineering!** ⭐

*Making AI more accessible, one prompt at a time.* 🚀