package promptgenerator.model;

public class ChineseCharacterInfo {
	private String character;
    private String characterLevel;
    private RadicalInfo radicals;
    
    public boolean isEmpty() {
    	if (character == null || character.trim().isEmpty()) {
    		return true;
    	}
    	return false;
    }

	public ChineseCharacterInfo(String character, String characterLevel, RadicalInfo radicals) {
		super();
		this.character = character;
		this.characterLevel = characterLevel;
		this.radicals = radicals;
	}

	public String getCharacter() {
		return character;
	}

	public void setCharacter(String character) {
		this.character = character;
	}

	public String getCharacterLevel() {
		return characterLevel;
	}

	public void setCharacterLevel(String characterLevel) {
		this.characterLevel = characterLevel;
	}

	public RadicalInfo getRadicals() {
		return radicals;
	}

	public void setRadicals(RadicalInfo radicals) {
		this.radicals = radicals;
	}
}
