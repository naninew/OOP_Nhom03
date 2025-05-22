package promptgenerator.model;

public class RadicalInfo {
	private String radical;
    private ChineseCharacterInfo originalCharacter;
    
    public boolean isEmpty() {
    	if (radical == null || radical.trim().isEmpty()) {
    		return true;
    	}
    	return false;
    }

	public RadicalInfo(String radical, ChineseCharacterInfo originalCharacter) {
		super();
		this.radical = radical;
		this.originalCharacter = originalCharacter;
	}

	public String getRadical() {
		return radical;
	}

	public void setRadical(String radical) {
		this.radical = radical;
	}

	public ChineseCharacterInfo getOriginalCharacter() {
		return originalCharacter;
	}

	public void setOriginalCharacter(ChineseCharacterInfo originalCharacter) {
		this.originalCharacter = originalCharacter;
	}
    
    
}
