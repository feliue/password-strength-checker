# password-strength-checker
A Python tool to analyze password strength - beginner cybersecurity project
# 🔐 Password Strength Checker

A beginner-friendly cybersecurity tool built in Python that analyzes password strength and provides detailed feedback to help users create stronger, more secure passwords.

---

## 📌 Features

- ✅ Checks password **length**
- ✅ Detects **uppercase and lowercase** letters
- ✅ Checks for **digits and special characters**
- ✅ Flags **commonly used passwords**
- ✅ Detects **repeated characters**
- ✅ Identifies **sequential patterns** (e.g. `123`, `abc`, `qwerty`)
- ✅ Gives an **overall strength score** with percentage
- ✅ Provides **actionable suggestions** to improve your password

---

## 🖥️ Demo

```
=======================================================
         PASSWORD STRENGTH ANALYZER
=======================================================
  Analyzing: ***********  (11 characters)
=======================================================

  📋 DETAILED ANALYSIS:
  --------------------------------------------------
  ✅ Length: Good length (12+ characters)
  ✅ Uppercase: Contains uppercase letters ✓
  ✅ Lowercase: Contains lowercase letters ✓
  ✅ Digits: Contains 2 digits ✓
  ✅ Special Characters: Contains 2 special characters ✓
  ✅ Common Passwords: Not a commonly known password ✓
  ✅ Repeated Characters: No excessive repeated characters ✓
  ✅ Sequential Patterns: No sequential patterns detected ✓

  🔐 OVERALL STRENGTH: 🟢 VERY STRONG
  📊 Score: 10/10 (100%)

  🎉 Great password! Keep it safe and don't reuse it.
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/password-strength-checker.git
```

2. Navigate to the project folder:
```bash
cd password-strength-checker
```

3. Run the tool:
```bash
python password_checker.py
```

---

## 📁 Project Structure

```
password-strength-checker/
│
├── password_checker.py   # Main script
└── README.md             # Project documentation
```

---

## 🛡️ How It Works

The tool runs your password through **8 security checks**, each contributing to a score out of 10. Based on your score:

| Score | Strength |
|-------|----------|
| 85–100% | 🟢 Very Strong |
| 65–84% | 🟡 Strong |
| 45–64% | 🟠 Moderate |
| 25–44% | 🔴 Weak |
| 0–24% | ⛔ Very Weak |

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or want to add a feature, feel free to open an issue.

---

## 📚 What I Learned

- Python functions and modular programming
- String manipulation and pattern detection
- Cybersecurity concepts around password security
- Writing clean, documented code

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 toyin 

**[Abdulhakeem Umar toyin]**  
Cybersecurity Student  
GitHub: [@YourUsername](https://github.com/YourUsername)
