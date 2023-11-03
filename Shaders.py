vrshad = """
    #version 450 core
    layout (location = 0) in vec3 pos;
    layout (location = 1) in vec2 txcrds;
    layout (location = 2) in vec3 nrms;
    uniform mat4 mdmat;
    uniform mat4 vmat;
    uniform mat4 pmat;    
    out vec2 UVs;
    out vec3 nrm;
    void main() {
        gl_Position = pmat * vmat * mdmat * vec4(pos, 1.0);
        UVs = txcrds;
        nrm = (mdmat * vec4(nrms, 0.0)).xyz;
    }
"""

frshad = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;    
    in vec2 UVs;
    in vec3 nrm;
    out vec4 fragColor;
    void main() {
        fragColor = texture(tex, UVs);
    }
"""
