package promptgenerator.model;

import java.util.List;

public class ChineseCharacterInfo {
	private String character;
    private String characterLevel;
    private List<String> radicals;
    
    public boolean isEmpty() {
    	if (character == null || character.trim().isEmpty()) {
    		return true;
    	}
    	return false;
    }
    
    public String toText() {
    	String result = "Character: " + character
    			+ "\nCharacter Level: " + characterLevel
    			+ "\nRadicals: \n";
    	int i = 1;
    	for (String radical : radicals) {
    		result = result + (i++) + ". " + radical + '\n';
    	}
    	return result;
    }

	public ChineseCharacterInfo(String character, String characterLevel, List<String> radicals) {
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

	public List<String> getRadicals() {
		return radicals;
	}

	public void setRadicals(List<String> radicals) {
		this.radicals = radicals;
	}
}
