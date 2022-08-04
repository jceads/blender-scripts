# blender-scripts
general purpose related to blender python scripts

# EXPORTER
blend_my_nft scriptine uygun hale getirilen blend dosyalarında çalışır. Önceki oluşuturulan nft koleksiyonunun json dosyaları gereklidir. 
Tüm meshlerin script ignore koleksiyonun içindeki armature a child edilmesi gerekiyor (düzgün vertex weightler ile) 
Armature sahnede görünür haldeyken çalıştırılmalıdır. <br>
Input: 
<ol>
<li>
Json dosyalarının olduğu klasör yolu girilmelidir
</li>
</ol>
Output: 
<ol>
<li>
tercih edilen yerde oluşturulan klasörün içerisine generate eder
</li>
</ol>
<br>

# External
blender ı ui açmadan çalıştırması gerekiyordu fakat çalışmıyor

# File size reducer
Klasörde olan png dosyalarının boyutunu düşürür
Önkoşul:
<ol>
<li>
Sistemde ffmpeg yüklü olması gerekiyor
</li>
<li>
Optimize edilecek png dosyalarının script ile aynı klasörde olması gerekiyor
</li>
</ol>

# Glb packer
Script ile açılacak glb dosyasının aynı klasörde olması gerekiyor. Büyük glb dosyalarının boyutunun küçültmeyi hedefler.
Şu anda çıktı olarak oluşturduğu glb dosyasında kullandığı orijinal boyuttaki png leri kullanıyor düzeltilmesi gerek
Herhangi bir input yok
Output:
<ol>
<li>
Optimize edilmiş glb dosyası
</li>
</ol>

# Rigger
exporter scriptinde uygulanan parent işlemi sayesinde bu script e gerek kalmamıştır. Amacı belirtilen armature diğer objeleri child etmektir.
