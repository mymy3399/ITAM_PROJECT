# ITAM_PROJECT - IT Asset Management Project

ITAM_PROJECT is a repository for an IT Asset Management system currently in early development phase. The repository contains minimal structure and is ready for development setup.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Current Repository State

This repository is currently minimal, containing only:
- `README.md` - Basic project title
- This instructions file

**IMPORTANT**: There are no existing build processes, dependencies, or runtime commands yet. All development infrastructure needs to be created.

## Working Effectively

### Important Timing and Timeout Guidelines
- **CRITICAL**: This repository currently has no build processes that require extended timeouts
- **Future Development**: When adding build processes, expect and set appropriate timeouts:
  - **Node.js builds**: May take 5-15 minutes - set timeout to 20+ minutes, NEVER CANCEL
  - **Maven builds**: May take 10-30 minutes - set timeout to 45+ minutes, NEVER CANCEL
  - **Python builds**: May take 3-10 minutes - set timeout to 15+ minutes, NEVER CANCEL
  - **Test suites**: May take 5-20 minutes - set timeout to 30+ minutes, NEVER CANCEL
- **NEVER CANCEL long-running operations** - Build and test processes need time to complete

### Initial Repository Setup
- Clone the repository: `git clone https://github.com/mymy3399/ITAM_PROJECT.git`
- Navigate to project: `cd ITAM_PROJECT`
- Verify contents: `ls -la` (should show README.md and .github directory)
- Check Git status: `git status`

### Development Environment
The development environment includes:
- **Operating System**: Ubuntu 24.04.3 LTS
- **Git**: 2.51.0
- **Node.js**: v20.19.4 (with npm 10.8.2)
- **Python**: 3.12.3 (with pip available)
- **Java**: OpenJDK (with Maven available)
- **Go**: Available for Go development
- **Docker**: Available for containerization

### Creating New Features
Since this is an empty repository, when adding new functionality:

1. **Determine Project Type**: Based on requirements, choose appropriate technology stack
2. **Initialize Project Structure**:
   - For Node.js projects: `npm init -y`
   - For Python projects: Create `requirements.txt`, `setup.py`, or `pyproject.toml`
   - For Java projects: Create `pom.xml` or Gradle build files
   - For Go projects: `go mod init github.com/mymy3399/ITAM_PROJECT`

3. **Set Up Development Infrastructure**:
   - Create appropriate `.gitignore` file
   - Add linting configuration (ESLint, Pylint, etc.)
   - Set up testing framework
   - Add CI/CD workflows in `.github/workflows/`

## Validation

### Git Workflow Validation
- **Always check git status**: `git status` before making changes
- **Verify branch**: `git branch -v` to confirm working branch
- **Review changes**: `git diff` before committing
- **Test commits**: Ensure commit messages are descriptive

### Code Quality Validation  
Since no linting/testing infrastructure exists yet:
- **Manual code review**: Carefully review all changes
- **Syntax validation**: Use appropriate language tools to check syntax
- **Future setup**: Add automated linting and testing as first development tasks

### Environment Validation
- **Tool availability**: Verify required development tools are installed
- **Path verification**: Check that commands are accessible via PATH
- **Permission check**: Ensure write permissions in project directory

### Manual Validation Requirements  
- **CRITICAL**: After making any changes, always perform manual validation scenarios
- **For web applications**: Test complete user workflows, not just startup/shutdown
- **For CLI tools**: Test with actual inputs and verify outputs are correct
- **For APIs**: Test endpoints with real requests and validate responses
- **Always test edge cases**: Empty inputs, invalid data, error conditions
- **Screenshot/document**: When possible, capture evidence of functional testing

## Common Tasks

### Repository Exploration
```bash
# View all files (excluding .git)
find . -type f | grep -v .git | sort

# Check repository size and structure  
du -sh . && echo "Files:" && find . -type f | wc -l

# View git history
git log --oneline --graph --all
```

### Initial Development Setup Examples

#### For Node.js/JavaScript Project:
```bash
npm init -y
npm install --save-dev eslint prettier jest
echo "node_modules/" >> .gitignore
npm run test  # After setting up test scripts
```

#### For Python Project:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
pip install --upgrade pip
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

#### For Java/Maven Project:
```bash
mvn archetype:generate -DgroupId=com.itam.project -DartifactId=itam-project -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd itam-project
mvn compile
mvn test
```

### File Operations
```bash
# Safe file viewing
cat README.md
head -20 [filename]  # View first 20 lines
tail -20 [filename]  # View last 20 lines

# Directory listing with details
ls -la
tree -a -I '.git'  # If tree is available
```

## Development Guidelines

### Adding New Components
1. **Plan first**: Document the component purpose and interface
2. **Create incrementally**: Start with minimal implementation
3. **Test early**: Add tests as you develop (not after)
4. **Document changes**: Update README.md and relevant docs

### Git Best Practices
- **Commit often**: Make small, focused commits
- **Clear messages**: Use descriptive commit messages
- **Branch appropriately**: Use feature branches for new work
- **Review before push**: Always review `git diff --cached` before committing

### Security Considerations
- **No secrets**: Never commit API keys, passwords, or credentials
- **Gitignore properly**: Exclude build artifacts, dependencies, logs
- **Review additions**: Check what files are being added with `git status`

## Troubleshooting

### Common Issues
1. **Empty repository feeling**: This is normal - the project is just starting
2. **No build commands**: Expected - infrastructure needs to be created first  
3. **Missing dependencies**: Normal for new project - add as needed
4. **Git confusion**: Use `git status` and `git log --oneline` to orient

### When Things Go Wrong
- **Check git status**: `git status` shows current state
- **Review recent changes**: `git diff HEAD~1` shows last commit changes  
- **Reset if needed**: `git checkout .` to discard working directory changes
- **Get help**: `git help [command]` for git command assistance

### Performance Notes
- **File operations**: Very fast - minimal files exist
- **Git operations**: Instant - small repository
- **Tool startup**: Standard - no heavy dependencies yet

## Future Development Areas

Based on the project name "ITAM_PROJECT" (IT Asset Management), likely development areas include:
- **Database integration**: For asset tracking
- **Web interface**: For asset management dashboard  
- **API development**: For system integration
- **Reporting features**: For asset analytics
- **Authentication**: For secure access
- **Import/Export**: For data migration

## Project Context

- **Repository**: https://github.com/mymy3399/ITAM_PROJECT
- **Current branch structure**: Multiple development branches exist
- **Development stage**: Initial/Planning phase
- **Technology stack**: To be determined based on requirements

Remember: This project is in its infancy. Most of your work will involve establishing the foundational development infrastructure and implementing core functionality from scratch.